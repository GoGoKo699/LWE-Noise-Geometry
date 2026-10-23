# LWE Noise Geometry

**Can two noise channels have matching local action, spectra, coherence, and quantum capacity, yet leave different computational learning problems?**

This project gives an explicit linear/cubic pair of correlated phase-noise channels for a coherent learning-with-errors (LWE) source. The linear source is exactly equivalent to lower-dimensional classical-input LWE. The cubic source permits full secret recovery by product Fourier measurements and classical linear algebra. Their difference survives a broad collection of matching channel diagnostics.

The hardness statement is conditional on quantum hardness of the specified classical-input LWE family. The coherent source is an additional, explicitly charged resource supplied by a holder who knows the secret. Ordinary lattice-based public keys do not supply that resource.

## Principal results

Let $`n\ge2`$ and let $`q\ge5`$ be prime with $`q\equiv2\pmod3`$. Uniform $`x\in\mathbb F_q^{n-1}`$ determines the phase label through one of two relations:

```math
z_{\mathrm{linear}}=\left(x,\sum_i x_i\right),
\qquad
z_{\mathrm{cubic}}=\left(x,\sum_i x_i^3\right).
```

| Property | Linear phase law | Cubic phase law |
|---|---|---|
| Computational measurement of each source copy | Ordinary $`n`$-dimensional LWE | The same LWE distribution |
| Every proper reduced input-noise channel | Complete computational dephasing | The same reduced channel |
| Per-secret source spectrum | $`\chi(e)/q^{n-1}`$, repeated $`q^{n-1}`$ times for each error label | The same spectrum |
| Nonzero normalized Choi spectrum | Uniform, rank $`q^{n-1}`$ | The same spectrum |
| Relative entropy of source coherence | $`\log_2 q`$ bits | $`\log_2 q`$ bits |
| Quantum capacity per complete channel use | $`\log_2 q`$ qubits | $`\log_2 q`$ qubits |
| Full-secret recovery | Equivalent to classical-input $`(n-1)`$-LWE | Polynomial time and a linear number of copies |

The [channel account](science/channels.md) also proves equal minimal environment dimension, bath entropy, average and entanglement fidelities, and unitarity. The complete channels have different superoperator spectra and can be distinguished efficiently using joint statistics from local Fourier measurements.

### Exact recovery with a fixed copy budget

The cubic learner recovers every secret with failure probability at most $`\delta`$ from

```math
N=\left\lceil
\frac{2n\ln q+\ln(1/\delta)}{\ln(q/3)}
\right\rceil
```

raw emitted copies, including discarded measurement outcomes. The calculation works for every additive-error law. A proved extension jointly learns fixed unknown nonzero cubic coefficients and a fixed offset. See [Secret recovery](science/learning.md).

### Exact fragility under independent local dephasing

For $`\Lambda_{p_j}=(1-p_j)\mathrm{Id}+p_j\Delta_j`$ acting on entire input field registers, both graph channels satisfy

```math
\left(\bigotimes_j\Lambda_{p_j}\right)\circ\mathcal D_\nu
=\eta\mathcal D_\nu+(1-\eta)\Delta_A,
\qquad
\eta=\prod_j(1-p_j).
```

The source then lies at trace distance exactly $`\eta(1-1/q)`$ from an ordinary classical $`n`$-dimensional LWE sample encoded in basis states. A fixed positive rate on every register makes this distance exponentially small. This supplies a conditional hardness reduction for the additionally dephased cubic source and identifies the ideal advantage's physical fragility. The [implementation account](science/implementation.md) gives the proof, circuit costs, accuracy budget, and a conservative small-noise success bound.

## Reading routes

| Goal | Route |
|---|---|
| Understand the scientific story | [Science guide](science/README.md) → [model and theorem](science/model.md) → [interpretation](science/interpretation.md) |
| Build the foundations and follow the result | [Learning guide](learning/README.md) → [30 milestones](learning/MILESTONES.md) with the [Watrous bridge](learning/WATROUS_BRIDGE.md) |
| Check the separation | [channel proofs](science/channels.md) → [LWE reduction](science/hardness.md) → [cubic learner](science/learning.md) |
| Assess physical assumptions | [source access](science/model.md#access-contract) → [implementation and perturbations](science/implementation.md) |
| Compare with earlier work | [related work](references/RELATED_WORK.md) and [BibTeX bibliography](references/references.bib) |
| Reproduce finite checks | [verification guide](verification/README.md) |
| Navigate with an LLM | [llms.txt](llms.txt) |

## Learning route

The single educational anchor is John Watrous's *The Theory of Quantum Information* (2018). The [bridge](learning/WATROUS_BRIDGE.md) selects the relevant sections, translates the book's channel notation into this project's finite-field source model, and works through a complete small cubic-recovery example.

The [30-milestone map](learning/MILESTONES.md) follows the project's logical dependencies. M01–M14 build the background and end by assembling the source model; M15–M30 develop the matched channel pair, the exact LWE reduction, the cubic learner, and the physical limits, ending in a synthesis of the full separation. The scientific proofs remain in their authoritative topic pages under [`science/`](science/README.md).

## Reproduce the finite checks

From the repository root, using Python 3.12:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py
```

The suite checks density operators, Fourier outcome probabilities, proper marginals, the hard-source simulator, exact modular recovery, the local-dephasing identity and distance, and finite information counterexamples. The [stored results](verification/expected_results.json) identify the actual parameter cases and numerical tolerances. These checks complement the proofs; they do not test cryptographic hardness.

## Consequential boundaries

The matched marginal statement applies to proper subsets of the noisy input registers, including retained references. Equal per-secret spectra do not imply equal Holevo information or identical many-copy statistical experiments. The [interpretation](science/interpretation.md) proves the equal information extracted by the actual Fourier readout and supplies counterexamples to stronger information claims.

The construction combines established quantum-example learning, polynomial interpolation, and dephasing-channel theory. [Related work](references/RELATED_WORK.md) gives the source-model comparisons and records one closely titled accepted paper whose full text was not located as of 2026-10-23. The repository makes no unqualified priority claim.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
