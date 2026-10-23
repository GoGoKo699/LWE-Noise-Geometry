"""Finite scientific checks for LWE Noise Geometry; not cryptographic tests.

Run with Python 3.12 and numpy 2.3.5. All modular calculations are exact.
Dense matrix checks use tolerance 1e-10 and only the explicitly listed grids.
"""

import argparse
import itertools
import json
import math
import platform
from collections import Counter
from pathlib import Path

import numpy as np

TOL = 1e-10


def grid(q, n):
    return np.array(list(itertools.product(range(q), repeat=n)), dtype=np.int64)


def rank_or_solve(matrix, rhs, q):
    """Exact modular elimination; solve only systems with full column rank."""
    a = np.array(matrix, dtype=np.int64).copy() % q
    if rhs is not None:
        a = np.column_stack((a, np.asarray(rhs, dtype=np.int64) % q))
    cols = a.shape[1] - (rhs is not None)
    rank, pivots = 0, []
    for col in range(cols):
        pivot = next((j for j in range(rank, len(a)) if a[j, col]), None)
        if pivot is None:
            continue
        a[[rank, pivot]] = a[[pivot, rank]]
        a[rank] = a[rank] * pow(int(a[rank, col]), -1, q) % q
        for j in range(len(a)):
            if j != rank:
                a[j] = (a[j] - a[j, col] * a[rank]) % q
        pivots.append(col)
        rank += 1
        if rank == len(a):
            break
    if rhs is None:
        return rank
    assert not np.any(np.all(a[:, :cols] == 0, axis=1) & (a[:, cols] != 0))
    assert rank == cols, (rank, cols)
    solution = np.zeros(cols, dtype=np.int64)
    solution[pivots] = a[:rank, cols]
    return solution


def entropy(probabilities):
    probabilities = np.real(np.asarray(probabilities))
    assert probabilities.min() > -TOL
    probabilities = probabilities[probabilities > 1e-12]
    return float(-np.sum(probabilities * np.log2(probabilities)))


def trace_one(rho, q, sites, omitted):
    tensor = rho.reshape((q,) * (2 * sites))
    result = np.trace(tensor, axis1=omitted, axis2=omitted + sites)
    return result.reshape(q ** (sites - 1), q ** (sites - 1))


def support(q, n, kind):
    x = grid(q, n - 1)
    last = x.sum(axis=1) if kind == "linear" else (x**3).sum(axis=1)
    return np.column_stack((x, last % q))


def bare_source(q, n, secret, chi):
    a = grid(q, n)
    dim = q ** (n + 1)
    rho = np.zeros((dim, dim), dtype=complex)
    for e, probability in enumerate(chi):
        vector = np.zeros(dim, dtype=complex)
        vector[np.arange(len(a)) * q + (a @ secret + e) % q] = 1 / math.sqrt(len(a))
        rho += probability * np.outer(vector, vector.conj())
    return rho


def phase_gram(q, a, z):
    omega = np.exp(2j * np.pi / q)
    phases = omega ** ((a @ z.T) % q)
    return phases @ phases.conj().T / len(z)


def expand_input_multiplier(gram, q):
    return np.repeat(np.repeat(gram, q, axis=0), q, axis=1)


def density_checks(q, n):
    """Compare explicit phase averaging, Fourier circuits, and LWE simulation."""
    a, x = grid(q, n), grid(q, n - 1)
    d, rsize = len(a), len(x)
    secret = (2 * np.arange(n) + 1) % q
    chi = np.arange(1, q + 1, dtype=float)
    chi /= chi.sum()
    rho = bare_source(q, n, secret, chi)
    omega = np.exp(2j * np.pi / q)
    fourier = omega ** np.outer(np.arange(q), np.arange(q)) / math.sqrt(q)
    full_fourier = fourier
    for _ in range(n):
        full_fourier = np.kron(full_fourier, fourier)
    states, grams, errors, coherence = {}, {}, {}, {}
    for kind in ("linear", "cubic"):
        z = support(q, n, kind)
        gram = phase_gram(q, a, z)
        grams[kind] = gram
        state = rho * expand_input_multiplier(gram, q)
        states[kind] = state
        eigs = np.linalg.eigvalsh(state)
        expected = np.sort(np.r_[np.repeat(chi / rsize, rsize),
                                 np.zeros(d * q - rsize * q)])
        errors[kind + "_source_spectrum"] = float(np.max(np.abs(eigs - expected)))
        # J is supported on span{|a,a>}; gram/d is its nonzero coordinate block.
        choi_eigs = np.linalg.eigvalsh(gram / d)
        expected_choi = np.r_[np.zeros(d - rsize), np.ones(rsize) / rsize]
        errors[kind + "_choi_spectrum"] = float(np.max(np.abs(choi_eigs - expected_choi)))
        coherence[kind] = entropy(np.diag(state)) - entropy(eigs)
        errors[kind + "_coherence"] = abs(coherence[kind] - math.log2(q))
        actual = np.real(np.diag(full_fourier @ state @ full_fourier.conj().T))
        expected_readout = np.zeros(d * q)
        for phase in z:
            for k in range(q):
                u = (-phase - k * secret) % q
                index = sum(int(u[j]) * q ** (n - 1 - j) for j in range(n))
                expected_readout[index * q + k] += 1 / (rsize * q)
        errors[kind + "_fourier_distribution"] = float(np.max(np.abs(actual - expected_readout)))
        for omitted in range(n):
            marginal = Counter(tuple(np.delete(phase, omitted)) for phase in z)
            assert len(marginal) == q ** (n - 1)
            assert set(marginal.values()) == {1}

    errors["same_diagonal"] = float(np.max(np.abs(
        np.diag(states["linear"]) - np.diag(states["cubic"]))))
    for omitted in range(n):
        left = trace_one(states["linear"], q, n + 1, omitted)
        right = trace_one(states["cubic"], q, n + 1, omitted)
        errors["source_marginal_omit_" + str(omitted)] = float(np.max(np.abs(left - right)))

    simulated = np.zeros_like(rho)
    quotient = int(secret[-1] - secret[:-1].sum()) % q
    for classical_x in x:
        for e, probability in enumerate(chi):
            vector = np.zeros(d * q, dtype=complex)
            classical_c = int(classical_x @ secret[:-1] + e) % q
            for y in range(q):
                labels = np.r_[(classical_x - y) % q, y]
                index = sum(int(labels[j]) * q ** (n - 1 - j) for j in range(n))
                vector[index * q + (classical_c + quotient * y) % q] = 1 / math.sqrt(q)
            simulated += probability / rsize * np.outer(vector, vector.conj())
    errors["hard_source_simulation"] = float(np.max(np.abs(simulated - states["linear"])))

    # Full matrix-unit check of the channel identity, not a random-input test.
    damping_cases = [
        np.full(n, 0.2),
        np.linspace(0.05, 0.4, n),
        np.r_[1.0, np.zeros(n - 1)],
    ]
    for case, probabilities in enumerate(damping_cases):
        eta = float(np.prod(1 - probabilities))
        damping = np.ones((d, d))
        for j, p in enumerate(probabilities):
            damping *= np.where(a[:, None, j] == a[None, :, j], 1.0, 1 - p)
        for kind in ("linear", "cubic"):
            gram = grams[kind]
            key = kind + "_dephasing_" + str(case)
            errors[key + "_channel_identity"] = float(np.max(np.abs(
                gram * damping - (eta * gram + (1 - eta) * np.eye(d)))))
            noisy_state = states[kind] * expand_input_multiplier(damping, q)
            classical = np.diag(np.diag(states[kind]))
            errors[key + "_source_identity"] = float(np.max(np.abs(
                noisy_state - eta * states[kind] - (1 - eta) * classical)))
            # Dense trace norm supplies an independent check of the exact constant.
            distance = float(np.abs(np.linalg.eigvalsh(noisy_state - classical)).sum() / 2)
            errors[key + "_trace_distance"] = abs(distance - eta * (1 - 1 / q))
            noisy_law = np.full(d, (1 - eta) / d)
            for phase in support(q, n, kind):
                index = sum(int(phase[j]) * q ** (n - 1 - j) for j in range(n))
                noisy_law[index] += eta / rsize
            alpha = (1 + (q - 1) * eta) / q
            formula = math.log2(q) - entropy([alpha, 1 - alpha]) - (1 - alpha) * math.log2(q - 1)
            errors[key + "_capacity_formula"] = abs(n * math.log2(q) - entropy(noisy_law) - formula)
            assert formula <= math.log2(1 + (q - 1) * eta**2) + TOL

    linear_abs, cubic_abs = np.abs(grams["linear"]), np.abs(grams["cubic"])
    errors["linear_superoperator_idempotent"] = float(np.max(np.abs(
        grams["linear"]**2 - grams["linear"])))
    assert np.any((cubic_abs > TOL) & (cubic_abs < 1 - TOL))
    assert np.all((linear_abs < TOL) | (linear_abs > 1 - TOL))
    linear_support = set(map(tuple, support(q, n, "linear")))
    cubic_support = set(map(tuple, support(q, n, "cubic")))
    tv = 1 - len(linear_support & cubic_support) / rsize
    assert tv >= 1 - 3 / q - TOL
    assert max(errors.values()) < TOL, errors
    return {"q": q, "n": n, "secret": secret.tolist(), "chi": chi.tolist(),
            "proper_noise_marginals_uniform": True, "coherence_bits": coherence,
            "phase_law_total_variation": tv, "numeric_errors": errors}


def regression_checks(q, n):
    """Generate graph outcomes independently of the claimed regression relation."""
    coordinates = [(u, k) for u in grid(q, n - 1) for k in range(1, q)]
    design = [np.r_[3 * u**2, 3 * k * u, k*k, -1] % q for u, k in coordinates]
    assert rank_or_solve(design, None, q) == 2 * n
    count = 0
    for secret in grid(q, n):
        rhs = []
        for u, k in coordinates:
            zfirst = (-u - k * secret[:-1]) % q
            zlast = sum(int(t)**3 for t in zfirst) % q
            un = (-k * int(secret[-1]) - zlast) % q
            rhs.append((un - sum(int(t)**3 for t in u)) * pow(k, -1, q) % q)
        solution = rank_or_solve(design, rhs, q)
        expected = np.r_[secret[:-1], secret[:-1]**2,
                         sum(int(t)**3 for t in secret[:-1]), secret[-1]] % q
        assert np.array_equal(solution, expected)
        count += 1
    return {"q": q, "n": n, "full_grid_rank": 2*n, "all_secrets_recovered": count}


def calibration_checks():
    q, n = 5, 2
    coordinates = [(u, k) for u in grid(q, n - 1) for k in range(q)]
    design = [np.r_[u**3, 3*k*u**2, 3*k*k*u, k**3, -k, -1] % q
              for u, k in coordinates]
    assert rank_or_solve(design, None, q) == 3*n
    recovered = 0
    for coefficients in itertools.product(range(1, q), repeat=n-1):
        c = np.asarray(coefficients)
        for offset in range(q):
            for secret in grid(q, n):
                rhs = []
                for u, k in coordinates:
                    zfirst = (-u - k * secret[:-1]) % q
                    zlast = int(offset + c @ (zfirst**3)) % q
                    rhs.append((-k * int(secret[-1]) - zlast) % q)
                result = rank_or_solve(design, rhs, q)
                expected = np.r_[c, c*secret[:-1], c*secret[:-1]**2,
                                 int(c @ (secret[:-1]**3)), secret[-1], offset] % q
                assert np.array_equal(result, expected)
                recovered += 1
    return {"q": q, "n": n, "full_grid_rank": 3*n,
            "all_coefficient_offset_secret_combinations_recovered": recovered}


def raw_copy_checks():
    """Deterministic replay of actual raw samples, charging k=0 outcomes."""
    rng = np.random.default_rng(20261023)
    results = []
    delta = 0.01
    for q, n in [(5, 2), (5, 5), (11, 4)]:
        raw_budget = math.ceil((2*n*math.log(q) + math.log(1/delta)) / math.log(q/3))
        assert (2*n*math.log(q) + raw_budget*math.log(3/q)) <= math.log(delta) + TOL
        discarded = []
        for _ in range(20):
            secret = rng.integers(q, size=n)
            design, rhs = [], []
            for _ in range(raw_budget):
                zfirst = rng.integers(q, size=n-1)
                z = np.r_[zfirst, sum(int(t)**3 for t in zfirst) % q]
                k = int(rng.integers(q))
                u = (-k*secret - z) % q
                if not k:
                    continue
                design.append(np.r_[3*u[:-1]**2, 3*k*u[:-1], k*k, -1] % q)
                rhs.append((int(u[-1]) - sum(int(t)**3 for t in u[:-1])) * pow(k, -1, q) % q)
            result = rank_or_solve(design, rhs, q)
            assert np.array_equal(np.r_[result[:n-1], result[-1]], secret)
            discarded.append(raw_budget - len(design))
        results.append({"q": q, "n": n, "delta": delta, "raw_budget": raw_budget,
                        "seeded_trials_passed": 20, "discarded_k_zero_per_trial": discarded})
    return results


def information_checks():
    q, n = 5, 2
    a = grid(q, n)
    laws = [[1., 0., 0., 0., 0.], [.5, .25, 0., 0., .25], [.2]*5]
    expected_values = [
        [3.788113094489, 3.713729014892],
        [2.557930866013, 2.571656843147],
        [1.857542475910, 1.857542475910],
    ]
    rows = []
    for chi, expected in zip(laws, expected_values):
        values = {}
        for index, kind in enumerate(("linear", "cubic")):
            z = support(q, n, kind)
            multiplier = expand_input_multiplier(phase_gram(q, a, z), q)
            average = np.zeros((q**(n+1), q**(n+1)), dtype=complex)
            for secret in a:
                average += bare_source(q, n, secret, chi) * multiplier / len(a)
            value = entropy(np.linalg.eigvalsh(average)) - ((n-1)*math.log2(q) + entropy(chi))
            assert abs(value - expected[index]) < TOL
            values[kind] = value
        rows.append({"chi": chi, "holevo_bits": values})
    # Exact readout MI from the entire joint distribution, independent of chi.
    mi = {}
    for kind in ("linear", "cubic"):
        z = support(q, n, kind)
        joint = np.zeros((len(a), len(a)*q))
        for si, secret in enumerate(a):
            for phase in z:
                for k in range(q):
                    u = (-phase-k*secret) % q
                    ui = sum(int(u[j])*q**(n-1-j) for j in range(n))
                    joint[si, ui*q+k] += 1 / (len(a)*len(z)*q)
        value = entropy(joint.sum(axis=0)) + entropy(joint.sum(axis=1)) - entropy(joint.ravel())
        assert abs(value - (1-1/q)*math.log2(q)) < TOL
        mi[kind] = value
    return {"q": q, "n": n, "ensemble_rows": rows, "fourier_mutual_information_bits": mi}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write JSON here; otherwise print to stdout.")
    args = parser.parse_args()
    report = {
        "checks_passed": True,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__},
        "tolerance": TOL,
        "density_cases": [density_checks(5, 2), density_checks(5, 3)],
        "exact_regression": [regression_checks(5, 2), regression_checks(5, 3)],
        "fixed_unknown_coefficients": calibration_checks(),
        "raw_copy_trials": raw_copy_checks(),
        "information_counterexamples": information_checks(),
    }
    output = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
        print("All finite checks passed; report written to", args.output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
