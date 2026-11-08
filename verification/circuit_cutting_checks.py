"""Finite q=5 channel-to-cutting checks; analytical converse lives in science/.

Construct the prescribed hidden-error branches and complete parity instrument.
Run: OPENBLAS_NUM_THREADS=1 python verification/circuit_cutting_checks.py
"""

import argparse
import json
import platform
from pathlib import Path

import numpy as np

TOL = 1e-11
D = 5


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def close(actual, expected, message):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    require(error < TOL, f"{message}: max error {error}")
    return error


def outer(vector):
    return np.outer(vector, vector.conj())


def phase_multiplier(kind):
    labels = np.array([(x, x if kind == "linear" else x**3 % D) for x in range(D)])
    inputs = np.array([(i, j) for i in range(D) for j in range(D)])
    phases = np.exp(2j * np.pi * (inputs @ labels.T) / D)
    return phases @ phases.conj().T / D


def parity_case(kind):
    eye = np.eye(D)
    ket = lambda j: eye[:, j]
    sym = lambda j: (ket(j) + ket(-j % D)) / np.sqrt(2)
    anti = lambda j: (ket(j) - ket(-j % D)) / np.sqrt(2)
    op = lambda a, b: np.outer(a, b.conj())
    ke = op(ket(0), ket(0)) + op(ket(1), sym(1)) + op(ket(2), sym(2))
    ko = op(ket(2), anti(1)) + op(ket(1), anti(2))
    completeness = close(ke.conj().T @ ke + ko.conj().T @ ko, eye,
                         "Decoder must include every physical outcome")
    psi = (np.kron(ket(1), sym(1)) + np.kron(ket(2), sym(2))) / np.sqrt(2)
    raw = np.zeros((D**4, D**4), dtype=complex)
    probabilities = np.zeros((2, 2))
    branch_rows = []
    for x in range(D):
        y = x if kind == "linear" else x**3 % D
        local = []
        for z in (x, y):
            phase = np.diag(np.exp(2j * np.pi * z * np.arange(D) / D))
            noisy = np.kron(eye, phase) @ psi
            local.append([np.kron(eye, k) @ noisy for k in (ke, ko)])
        row = []
        for a in range(2):
            for b in range(2):
                vector = np.kron(local[0][a], local[1][b])
                probability = float(np.vdot(vector, vector).real)
                probabilities[a, b] += probability / D
                score = 1 if a == b else -1  # No hidden-error input to this rule.
                raw += score * outer(vector) / D
                row.append(probability)
        close(sum(row), 1, "Complete outcome probability conditional on hidden error")
        branch_rows.append({"hidden_error": x, "outcome_probabilities_ee_eo_oe_oo": row})
    # Convert temporal local order A1,A2,B1,B2 into slot order A1,B1,A2,B2.
    raw = raw.reshape((D,) * 8).transpose(0, 2, 1, 3, 4, 6, 5, 7).reshape(D**4, D**4)
    phi_vector = sum(np.kron(ket(j), ket(j)) for j in range(D)) / np.sqrt(D)
    phi = outer(phi_vector)
    ident = np.eye(D * D)
    trace_product = lambda a, b: float(np.einsum("ij,ji->", a, b).real)
    moments = [float(np.trace(raw).real),
               trace_product(np.kron(phi, ident), raw),
               trace_product(np.kron(ident, phi), raw),
               trace_product(np.kron(phi, phi), raw)]
    moment_error = close(moments, [1/4, 1/20, 1/40, 1/40], "Four scored moments")
    t, f1, f2, f12 = moments
    sectors = [f12, f1-f12, f2-f12, t-f1-f2+f12]
    close(sectors, [1/40, 1/40, 0, 1/5], "All twirled sectors")
    r = (ident - phi) / 24
    twirled = sum(p * np.kron(a, b) for p, a, b in zip(
        sectors, (phi, phi, r, r), (phi, r, phi, r)))
    rho_plus = phi/5 + 4*r/5
    reconstructed = (5*np.kron(rho_plus, rho_plus) + 32*twirled
                     - 8*np.kron(rho_plus, r) - 4*np.kron(r, rho_plus))
    matrix_error = close(reconstructed, np.kron(phi, phi), "Full extent-49 identity")
    close(probabilities.sum(), 1, "Unconditional instrument completeness")
    close(np.trace(probabilities), 5/8, "Charged same-parity probability")
    close(probabilities.sum() - np.trace(probabilities), 3/8,
          "Negative cross-parity outcomes cannot be omitted")
    return raw, {"channel": kind, "decoder_completeness_max_error": completeness,
                 "branch_rows": branch_rows,
                 "outcome_probabilities_ee_eo_oe_oo": probabilities.ravel().tolist(),
                 "scored_moments_trace_first_second_joint": moments,
                 "moments_max_error": moment_error,
                 "sector_coefficients": sectors,
                 "full_625_by_625_identity_max_error": matrix_error,
                 "coefficient_extent": 5+32+8+4}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    linear, linear_report = parity_case("linear")
    cubic, cubic_report = parity_case("cubic")
    same_atom_error = close(linear, cubic, "The actual scored parity resources must agree")
    channel_difference = float(np.max(np.abs(phase_multiplier("linear") - phase_multiplier("cubic"))))
    require(channel_difference > .1, "Equal cutting atoms must not be mistaken for equal channels")
    for x in range(D):
        require(x**3 % D in (x, -x % D), "Required q=5 cube/parity identity")
    require(any(x**3 % 11 not in (x, -x % 11) for x in range(11)),
            "The parity identity must not be advertised for arbitrary allowed primes")
    report = {"checks_passed": True, "runtime": {"python": platform.python_version(),
               "numpy": np.__version__}, "tolerance": TOL,
              "cases": [linear_report, cubic_report],
              "linear_cubic_scored_atom_max_error": same_atom_error,
              "linear_cubic_channel_multiplier_max_difference": channel_difference,
              "scope": "Finite complete-instrument and resource identities; timing, universal witness and operational closure are analytical."}
    result = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
        print("All q=5 circuit-cutting checks passed; report written to", args.output)
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
