# Related work and source models

The comparison in this repository concerns the computational effect of two known distributions of correlated local phase errors on the same coherent-example source. It combines established Fourier-learning, dephasing-channel, and polynomial-interpolation techniques. The contribution is the simultaneous matching of specified channel and state properties while the resulting secret-recovery tasks have different computational complexity. The hard side is conditional on the stated quantum hardness assumption for classical LWE.

Citation keys below correspond to [references.bib](references.bib). Links point to primary papers, author manuscripts, or official publication records. Source versions and the outstanding closest-title comparison are recorded at the end.

## 1. The access model matters

Classical LWE supplies independent pairs

```math
 a\leftarrow\mathbb F_q^n,\qquad b=\langle a,s\rangle+e,\qquad e\leftarrow\chi.
```

Regev's reduction connects appropriate parameter families to worst-case lattice problems; it does not prove an unconditional lower bound for LWE ([regev2009](https://cims.nyu.edu/~regev/papers/qcrypto.pdf)). The source studied here instead supplies independent copies of

```math
 \rho_s^\nu=\mathbb E_{e\sim\chi,z\sim\nu}
 Z_A(z)|\psi_{s,e}\rangle\langle\psi_{s,e}|Z_A(z)^\dagger,
 \qquad
 |\psi_{s,e}\rangle=q^{-n/2}\sum_a|a\rangle|\langle a,s\rangle+e\rangle.
```

Within one preparation, a single classical error $`e`$ is common to all coherent branches. Both $`e`$ and the phase label $`z`$ are freshly sampled between copies. The public noise law $`\nu`$ is independent of the secret. Measuring the computational basis gives the classical LWE distribution, but possession of classical LWE samples does not by itself provide this coherent source.

| Model | Coherent variable | Error representation | Relevant source |
|---|---|---|---|
| Classical LWE | None | Classical additive error | [regev2009](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) |
| Present common-error source | Input $`a`$ | One sampled $`e`$ shared across branches, followed by random phases on $`A`$ | Definition above |
| Noisy quantum LWE examples | Input $`a`$ | Branch-dependent errors $`e_a`$ | [grilo2019](https://arxiv.org/pdf/1702.08255v2), Sections II–IV and Appendix C |
| $`\mathsf{S\lvert LWE\rangle}`$ | Error variable | Complex amplitudes $`f(e)`$, with classical $`a`$ | [chen2022](https://arxiv.org/abs/2108.11015), [chen2025](https://arxiv.org/html/2310.00644v2), Definition 2 |

These models cannot be interchanged in a hardness or preparation argument. Here a party that knows $`s`$ can prepare the common-error source with reversible modular arithmetic. This preparation statement does not grant an adversary a coherent public-key oracle, and no QRAM construction from a table of classical samples is assumed.

## 2. Noisy quantum examples and Fourier learning

Cross, Smith, and Smolin show efficient quantum parity learning under independent local depolarization, while the corresponding classical examples produce LPN. Their analysis already includes an input-independent parity error. Thus common label noise and the use of Fourier measurements to extract a hidden linear function are established ingredients ([cross2015](https://arxiv.org/abs/1407.5088); [published version](https://doi.org/10.1103/PhysRevA.92.012327)).

Grilo, Kerenidis, and Zijlstra extend quantum-example learning to LWE with branch-dependent errors. Their model samples an entire error function and traces out its randomness; the principal case uses independent $`e_a`$. They prove efficient recovery for appropriate bounded-error regimes and explain the distinction from ordinary LWE cryptography. Their Section II expressly identifies the preparation cost that may accompany independent errors on exponentially many branches ([grilo2019](https://arxiv.org/pdf/1702.08255v2)). The present source uses the simpler common-error preparation; the new comparison is between correlated phase channels applied after that preparation.

The Fourier observation $`u=-ks-z`$, with a measured label frequency $`k`$, is a direct application of character orthogonality and phase kickback. It is not a new Fourier algorithm. The finite-precision implementation can use standard phase-estimation and gate-compilation tools ([cleve1998](https://arxiv.org/abs/quant-ph/9708016), [dawson2006](https://arxiv.org/abs/quant-ph/0505030)).

Ma, Su, and Deng study correction of noisy Fourier samples and verification of quantum learning. Their correlated-noise extension imposes a sufficiently small error probability on each output bit. That hypothesis differs from the present channels, whose every proper phase-coordinate marginal is uniform ([ma2024](https://arxiv.org/html/2411.09210v1), Supplement, Theorem S2). Their result should not be interpreted as a robustness guarantee for the exact global correlations used here.

## 3. Quantum LWE amplitudes and phase-dependent complexity

Chen, Liu, and Zhandry introduce and study LWE-like states with coherent error amplitudes, obtaining algorithms through quantum filtering ([chen2022](https://arxiv.org/abs/2108.11015)). In this model, $`a`$ is classical and the sample's quantum register has the form $`\sum_e f(e)|\langle a,s\rangle+e\rangle`$.

Chen, Hu, Liu, Luo, and Tu give algorithms for known amplitude functions, polynomial-time algorithms for suitable complex Gaussian amplitudes with quadratic phases, and hardness reductions for Gaussian amplitudes with small unknown phase terms ([chen2025](https://doi.org/10.1007/978-3-032-01878-6_17)). The explicit phase model in Definition 7 of the [arXiv full text](https://arxiv.org/html/2310.00644v2) includes auxiliary classical information and a phase function that need not be efficiently computable; Sections 5–6 use that distinction in their reductions. These results establish that phase information can change quantum-LWE learnability.

The present comparison fixes a different source and two fully specified classical distributions of local phase gates. Its matched quantities concern mixed output states and channel Choi states, as well as proper reduced channels and block capacity. It does not replace the amplitude-learning results or make the unknown phases in their hardness reductions available. The known/unknown phase distinction and the location of coherence are essential when comparing the two settings.

## 4. Linear information and noisy stabilizer decoding

Exact linear information about a secret can reduce the dimension of an LWE instance. More general integration of secret and error hints into lattice attacks is studied by Dachman-Soled, Ducas, Gong, and Rossi ([dachmansoled2020](https://doi.org/10.1007/978-3-030-56880-1_12)). Dimension reduction itself is therefore not the new ingredient. The subspace-noise result here identifies precisely which linear information is revealed by coherent sampling and gives both source transformations: extraction of residual classical LWE, and simulation of the noisy quantum source from residual LWE plus known complementary secret coordinates.

Poremba, Quek, and Shor define Learning Stabilizers with Noise as recovery of an unknown codeword in a known random stabilizer code under independent local depolarization. They give algorithms in several noise regimes, reductions, and applications to computational limitations of quantum-data learning ([poremba2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.108/LIPIcs.ITCS.2026.108.html), Sections 2 and 4–5). That task differs from learning an unknown linear-function parameter under two known correlated phase laws. It supplies relevant context for computational hardness in noisy stabilizer-based inputs, rather than the matched-channel comparison made here.

## 5. Hidden polynomial graphs and interpolation

Decker and Wocjan study hidden polynomial function graphs through a level-set oracle and quantum state identification, including efficient algorithms for quadratic and cubic graphs ([decker2007](https://arxiv.org/abs/quant-ph/0703195)). Rötteler studies quadratic hidden shifts and functions close to quadratics, and explicitly relates exact quadratic-shift reconstruction by linear algebra to noisy parity learning ([roetteler2009](https://arxiv.org/html/0911.4724v1), Section 3).

These are precedents for replacing linear structure with low-degree polynomial structure. The present learner receives ordinary classical points on a translated, publicly known graph after its Fourier measurement. Expanding the cubic constraint gives a linear system in lifted secret coefficients. This interpolation step uses standard polynomial algebra; it is not an algorithm for the more general hidden-graph oracle problem. The role of the cubic graph is to supply a recoverable distribution whose proper phase-coordinate marginals match those of the linear graph exactly.

## 6. Coherence, channel diagnostics, and capacity

Relative entropy of coherence is an established basis-dependent quantity ([baumgratz2014](https://arxiv.org/abs/1311.0275)). For the present source, orthogonality of the $`(e,z)`$-labelled pure components gives eigenvalues $`\chi(e)\nu(z)`$, and hence

```math
 C_{\mathrm{rel}}(\rho_s^\nu)=n\log_2 q-H(\nu).
```

Matching this scalar does not contradict coherence monotonicity or imply that arbitrary tasks must have equal difficulty. The comparison retains the same computational basis and derives the additional matches explicitly.

Average gate fidelity and unitarity are standard channel diagnostics ([nielsen2002](https://arxiv.org/abs/quant-ph/0205035), [wallman2015](https://arxiv.org/abs/1503.07865)). The equality of the normalized Choi spectra must be distinguished from equality of the channel superoperator spectra. The linear-support channel is idempotent; the cubic-support channel has different Fourier multipliers. Equal Choi spectra do not erase that distinction.

The quantum-capacity theorem and the single-letter structure of degradable channels are inherited results ([devetak2005](https://arxiv.org/abs/quant-ph/0304127), [devetakshor2005](https://arxiv.org/html/quant-ph/0311131v3)). D'Arrigo, Benenti, and Falci analyze correlated dephasing, including the optimal maximally mixed input for correlated Pauli phase errors ([darrigo2007](https://arxiv.org/html/quant-ph/0703014v3), Sections 2–3). For the fixed $`n`$-register random-phase channel used independently between blocks, the same degradability and covariance argument gives

```math
 Q(\mathcal D_\nu)=n\log_2 q-H(\nu).
```

The repository derives the finite-field specialization and the resulting equality for its two channels. This is an application of known capacity theory. Communication capacity concerns optimized encodings and decodings; it does not by itself characterize inference from a prescribed unknown-secret source.

## 7. Global correlations, reduced channels, and additional dephasing

Harper, Flammia, and Wallman characterize correlated Pauli noise and explain why scalar diagnostics do not determine the full noise model ([harper2020](https://arxiv.org/html/1907.13022v2)). Liu and Wild obtain efficient local-to-global reconstruction under decay of conditional mutual information ([liuwild2026](https://arxiv.org/abs/2603.07037)). The exact global constraints here do not satisfy a general assumption that proper marginals determine the joint distribution.

For either graph law, omitting any one phase coordinate leaves a uniform marginal. The supports are orthogonal arrays of strength $`n-1`$ and index one. Orthogonal arrays and the use of their balanced marginals in quantum control are established; Rötteler and Wocjan connect them to local decoupling schemes ([roettelerwocjan2006](https://arxiv.org/html/quant-ph/0409135v1), Sections 4.3 and 5.3). The two supports are themselves related by independent permutations of the first $`n-1`$ alphabets. Their combinatorial equivalence does not give a secret-independent conversion between the encoded learning states, as [Interpretation](../science/interpretation.md) explains.

The all-proper-marginal property is therefore an inherited combinatorial ingredient, not a new tomography principle. Full joint phase samples can be obtained using product $`|+\rangle`$ probes and local Fourier measurements; global processing then distinguishes the known laws. The comparison does not establish a lower bound on tomography using product measurements.

Independent local dephasing multiplies a matrix element by a factor for each coordinate on which its indices differ. The present support condition makes every surviving off-diagonal element have full coordinate support. Consequently, for $`\Lambda_{p_j}=(1-p_j)\mathrm{Id}+p_j\Delta_j`$,

```math
 \left(\bigotimes_j\Lambda_{p_j}\right)\circ\mathcal D_\nu
 =\eta\mathcal D_\nu+(1-\eta)\Delta_A,
 \qquad \eta=\prod_j(1-p_j).
```

The multiplication of independent dephasing factors is standard channel physics; the exact identity is a consequence of the graph-law marginal constraint. Its application here quantifies the fragility of the learning advantage. In particular, the ideal correlated-noise theorem is not a constant-rate fault-tolerance statement.

## 8. What the comparison establishes

For the specified linear and cubic graph laws, the following ingredients are combined in one source family:

- identical computational-basis sample distributions and learning-state spectra;
- identical normalized Choi spectra and every proper reduced phase-noise channel;
- equal relative entropy of coherence and quantum capacity;
- an exact equivalence to residual classical LWE for linear support;
- polynomial-copy secret recovery by Fourier sampling and lifted regression for cubic support.

The individual tools above are inherited or elementary. The repository's assertion is this restricted simultaneous comparison and its reductions, not a general ordering of noise channels by usefulness, an unconditional quantum lower bound, or an attack on standard LWE ciphertexts. Full channel knowledge is available to the learner on both sides.

## 9. Version and coverage notes

**Chen et al.** The published record is CRYPTO 2025, LNCS 16001, pp. 513–544, DOI 10.1007/978-3-032-01878-6_17. The [ePrint record](https://eprint.iacr.org/2023/1498) identifies a 2025-06-22 revision. The full text inspected for the definitions and section-level comparison is arXiv:2310.00644v2, dated 2024-10-06; it is not asserted to be identical to the later ePrint revision. The publisher and current ePrint abstracts confirm the known-amplitude, complex-Gaussian, and unknown-phase distinction. The current ePrint PDF and the publisher's full chapter were not accessible in this check.

**Pirnay and Seifert.** [pirnay2026](https://acm-pqqs.github.io/pqqs2026/call-for/accepted-papers.html), *On linearly derived quantum samples for LWE*, is listed as accepted at ACM PQQS 2026. The [official program](https://acm-pqqs.github.io/pqqs2026/call-for/detailed-program.html) schedules it for November 3, 2026. As of 2026-10-23, a full manuscript was not located through the official conference pages, the [authors' institutional publication listing](https://www.tu.berlin/en/sect/publications), arXiv, ePrint, ACM, or a title-based Crossref lookup. The institutional listing's file link points to the conference homepage. These records establish the paper's existence, not its results. No assertion of priority or non-overlap relative to that paper is made here.

This account distinguishes the inspected results and their access assumptions. It does not certify exhaustive novelty.
