# Finite verification

The suite independently constructs the source density matrices, simulates the hard-source reduction, generates phase labels, and solves the resulting finite-field systems. It checks identities that carry the main claims and counterexamples that rule out stronger interpretations.

The general statements are proved in [science/](../science/README.md). Finite checks do not establish an asymptotic LWE hardness assumption, a quantum-capacity coding theorem, experimental feasibility, or priority.

## Run

From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py
```

To save a fresh report:

```bash
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py --output /tmp/lwe_noise_geometry_results.json
```

The recorded run used Python 3.12.14 and NumPy 2.3.5. NumPy is the only third-party dependency. Limiting BLAS threads avoids excessive thread overhead on these small matrices; it does not change the algorithm or the claimed tolerances.

The script exits unsuccessfully if any check fails. A successful run prints JSON with `"checks_passed": true`. The checked-in [expected_results.json](expected_results.json) contains the reference run. Floating-point last digits may differ across supported linear-algebra backends; the meaningful comparison uses the documented tolerances and exact integer results, not byte-for-byte equality.

## What is checked

| Check | Cases and method | Connection to the science |
|---|---|---|
| Full source spectra | Explicit phase averaging of dense density matrices at $`q=5,n=2,3`$ | Factorized spectrum $`\nu(z)\chi(e)`$ |
| Normalized Choi spectra | Diagonalize the Choi state's nonzero coordinate block | Uniform rank $`q^{n-1}`$ |
| Source diagonal and coherence | Compare full matrices and spectral entropies | Same classical LWE samples and $`\log_2q`$ coherence |
| Proper noise marginals | Enumerate every projection omitting one coordinate | Bijective graph projections; smaller marginals follow |
| Reduced source states | Explicit partial trace of each input register | Equality even while retaining the output register |
| Fourier readout | Dense tensor Fourier circuit compared with generated phase-law probabilities | Correct sign and complete distribution $`u=-ks-z`$ |
| Hard-source simulator | Build the coherent fiber separately from classical residual-LWE samples | Exact $`(n-1)`$-LWE simulation |
| Cubic recovery | Exact modular elimination over the full feature grid; every secret at $`q=5,n=2,3`$ | Ranks 4 and 6; all 25 and 125 secrets recovered |
| Unknown fixed coefficients | Every nonzero coefficient, offset, and secret at $`q=5,n=2`$ | Rank 6; all 500 combinations recovered |
| Raw-copy accounting | 20 seeded runs each at $`(q,n)=(5,2),(5,5),(11,4)`$ | Fixed budget includes every $`k=0`$ outcome |
| Dephasing identity | Every channel matrix unit at $`q=5,n=2,3`$, with uniform, heterogeneous, and one-site complete dephasing | Exact mixture with complete input dephasing |
| Dephasing distance | Dense trace norms of the noisy and classical source difference | Exact factor $`\eta(1-1/q)`$ |
| Capacity along the mixture | Direct entropy of the broadened phase law | Closed form and order-two upper bound |
| Channel distinctions | Full multiplier matrix and support intersection | Linear idempotence, fractional cubic multipliers, total variation |
| Information counterexamples | Average dense matrices over all 25 secrets, for three error laws | Unequal Holevo information despite equal conditional spectra |
| Fourier mutual information | Entire joint distribution of secret and readout | Equal $`(1-1/q)\log_2q`$ bits |

All modular calculations are exact. Dense numerical checks require absolute error below $`10^{-10}`$. They use a nonuniform error law with positive probabilities proportional to $`1,2,\ldots,q`$, unless the information-counterexample table specifies another law.

The seeded trials are deterministic examples of the complete measurement-to-recovery pipeline, not a statistical proof of the copy bound. The bound itself follows from the product-grid polynomial argument in [learning.md](../science/learning.md#proof-of-the-copy-bound). The script uses exhaustive grids only for tiny finite instances; the actual learner never enumerates those grids.

## Interpreting a successful run

A pass supports consistency among the equations, sign conventions, simulator, and executable finite examples. The capacity check evaluates the derived entropy expression; it does not independently prove the degradable-channel capacity theorem. The dephasing check covers all matrix units in the stated finite spaces, while the arbitrary-dimension channel identity is established analytically.

The error-free and uniform-error information examples are deliberate limiting cases. They are not presented as secure LWE parameters. The narrow nonuniform example shows that matching each secret-conditioned spectrum does not generally match the ensemble information, and the direction of the difference can reverse.
