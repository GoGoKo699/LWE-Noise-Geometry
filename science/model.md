# Source model and separation theorem

[Science guide](README.md) · [Channel invariants](channels.md) · [Hardness](hardness.md) · [Learning](learning.md)

## The question

A noise channel has many useful summaries: its local action, environment entropy, Choi spectrum, coherence loss, and quantum capacity. These summaries do not specify how the remaining coherence is aligned with an unknown parameter. This project constructs two correlated phase-noise channels for which those summaries agree, yet recovering the secret encoded in their output states has different computational complexity.

The secret is the coefficient vector in a learning-with-errors (LWE) sample. The construction concerns a specified quantum source that knows that secret. Ordinary classical LWE samples and lattice-based public keys do not provide this source. Its access model is part of the theorem.

## Registers, arithmetic, and distributions

Let $`n\ge 2`$ and let $`q\ge 5`$ be a prime satisfying $`q\equiv 2\pmod 3`$. All register labels and polynomial expressions are in $`\mathbb F_q`$. The map $`x\mapsto x^3`$ is a permutation because $`\gcd(3,q-1)=1`$.

The input comprises $`n`$ registers $`A_1,\ldots,A_n`$, each of dimension $`q`$. The output register $`B`$ also has dimension $`q`$. Write $`A=A_1\cdots A_n`$, $`d=q^n`$, and $`\omega=e^{2\pi i/q}`$.

The secret $`s\in\mathbb F_q^n`$ is fixed across emissions. Average-case hardness refers to a uniformly sampled secret. The scalar error distribution $`\chi`$ on $`\mathbb F_q`$ is public and efficiently samplable. For identities and the easy learner it may be arbitrary; the computational separation additionally assumes a quantum-hard classical-input LWE regime.

Unless marked $`\ln`$, all entropies and logarithms are in bits. Trace distance is $`D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1`$; channel distance uses the corresponding half diamond norm. Quantum capacity is counted in qubits per invocation of the entire $`n`$-register channel, with independent invocations.

## An emitted quantum sample

One emission draws one scalar error $`e\sim\chi`$ and prepares

```math
|\psi_{s,e}\rangle
=q^{-n/2}\sum_{a\in\mathbb F_q^n}|a\rangle_A|a\cdot s+e\rangle_B.
```

The same $`e`$ occurs in every coherent branch of this emission. A fresh independent $`e`$ is drawn for the next emission. This is different from assigning independently drawn errors $`e_a`$ to different branches.

For a public distribution $`\nu`$ on $`\mathbb F_q^n`$, define the random-phase channel

```math
Z_z|a\rangle=\omega^{z\cdot a}|a\rangle,\qquad
\mathcal D_\nu(X)=\sum_z\nu(z)Z_zXZ_z^\dagger.
```

It acts on $`A`$ only. The learner receives independent copies of

```math
\rho_s^\nu
=(\mathcal D_\nu\otimes\mathrm{Id}_B)
\left(\sum_e\chi(e)|\psi_{s,e}\rangle\langle\psi_{s,e}|\right).
```

The phase draw $`z`$ is independent of $`e`$ and $`s`$. Neither draw is revealed.

### Access contract

The source holder knows $`s`$ and can implement the controlled modular addition needed to prepare the state. The learner receives state copies, with no access to the source's seed, purification, inverse circuit, or internal error and phase registers. The learner does not choose $`a`$ or obtain multiple chosen inputs under the same $`e`$.

A computational-basis measurement of one copy gives exactly

```math
a\leftarrow U(\mathbb F_q^n),\qquad b=a\cdot s+e,\qquad e\leftarrow\chi,
```

for every phase law $`\nu`$. The classical baseline therefore consists of ordinary independent classical LWE samples. A quantum adversary against that baseline may perform arbitrary quantum computation on the classical data. This is the meaning of **classical-input LWE**.

There is no free QRAM assumption. Preparation, randomness, Fourier transforms, and classical processing are charged in [Implementation and perturbations](implementation.md). Granting coherent source access is an additional physical resource; it is not inferred from a classical public key.

## Two phase distributions

For $`x=(x_1,\ldots,x_{n-1})`$ uniform in $`\mathbb F_q^{n-1}`$, define

```math
L=\left\{\left(x,\sum_{i=1}^{n-1}x_i\right):x\in\mathbb F_q^{n-1}\right\},
\qquad
C=\left\{\left(x,\sum_{i=1}^{n-1}x_i^3\right):x\in\mathbb F_q^{n-1}\right\}.
```

Let $`\nu_L`$ and $`\nu_C`$ be uniform on $`L`$ and $`C`$, respectively. Both supports contain $`R=q^{n-1}`$ points. The first is a linear hyperplane; the second is a cubic graph. All choices are explicit and secret-independent.

For example, at $`n=2,q=5`$, the possible phase labels are:

| First label | Linear last label | Cubic last label |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 2 |
| 4 | 4 | 4 |

Each individual phase label is uniform in both cases. The distinction lies in the relation between labels.

## Main theorem

For the source and distributions just defined, the following statements hold.

1. **Matching diagnostics.** The two channels have the same action on every proper subset of input registers, even with a reference. The two per-secret source states have the same computational diagonal and full spectrum. Their relative entropy of coherence, normalized Choi spectra, minimal environment dimensions, environment entropy for the maximally mixed input, entanglement and average gate fidelities, unitarity, and quantum capacities agree. In particular, the relative entropy of coherence and the capacity are both $`\log_2 q`$ in their respective units. The precise domains and proofs are in [Channel invariants](channels.md).

2. **Hard branch.** Learning $`s`$ from copies of $`\rho_s^{\nu_L}`$ is polynomially equivalent to recovering a uniform secret from ordinary classical-input $`(n-1)`$-dimensional LWE with the same $`q,\chi`$. One additional secret coordinate combination is directly accessible. The reduction holds against arbitrary collective quantum processing of source copies; it does not restrict the learner to the Fourier measurement. See [Hardness](hardness.md).

3. **Easy branch.** A product Fourier measurement followed by classical modular linear algebra recovers every $`s`$ from copies of $`\rho_s^{\nu_C}`$ with failure probability at most $`\delta`$, for any $`0<\delta<1`$. A sufficient fixed raw-copy budget is

```math
N=\left\lceil
\frac{2n\ln q+\ln(1/\delta)}{\ln(q/3)}
\right\rceil.
```

This is $`O(n+\log(1/\delta))`$ uniformly for the allowed primes. The algorithm is independent of the error law $`\chi`$ and requires no collective quantum memory. Its polynomial-time proof is in [Learning](learning.md).

4. **Exact fragility.** Apply independent computational-dephasing mixtures
   $`\Lambda_{p_j}=(1-p_j)\mathrm{Id}+p_j\Delta_j`$
   to the input registers after either correlated channel. With
   $`\eta=\prod_j(1-p_j)`$, the resulting source is exactly

```math
\widetilde\rho_s^\nu
=\eta\rho_s^\nu+(1-\eta)\rho_s^{\mathrm{cl}},
\qquad
\rho_s^{\mathrm{cl}}
=q^{-n}\sum_{a,e}\chi(e)|a,a\cdot s+e\rangle\langle a,a\cdot s+e|.
```

Its trace distance from the classical source is exactly $`\eta(1-1/q)`$. For $`m`$ independent copies, the distance is at most $`m\eta(1-1/q)`$. A common fixed rate $`p>0`$, or heterogeneous rates bounded below by such a constant, makes polynomially many copies exponentially close to classical **$`n`$-dimensional** LWE. Under the corresponding quantum-hardness assumption, efficient recovery is then impossible with nonnegligible success. The channel identity and reduction are proved in [Implementation and perturbations](implementation.md).

The diagnostic identities, exact reductions, copy bound, and dephasing identity are unconditional mathematical results. All **computational-hardness conclusions**, including the hard/easy separation and the noisy-source consequence, are conditional on their specified classical-input LWE assumptions. No unconditional exponential lower bound is asserted.

### Parameter meaning

An asymptotic security claim specifies a family $`q=q(n)`$ and $`\chi=\chi_n`$, and a quantum-polynomial-time average-case search-LWE assumption for that family. One may take polynomial-size primes in the required residue class and an efficiently sampled narrow error law in a conventional LWE regime. The residue restriction guarantees the permutation used in the construction; it is not a substitute for the hardness assumption.

The relevance of LWE to worst-case lattice problems is an established reduction, not a proof that a particular finite instance is hard. [Regev's original LWE paper](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) supplies that background; [Hardness](hardness.md) states the exact assumption needed here. Tiny finite examples in the verification suite test identities, not cryptographic security.

## A useful factorization

Let $`|+\rangle=q^{-n/2}\sum_a|a\rangle`$, let $`\mathrm{diag}\,\chi=\sum_e\chi(e)|e\rangle\langle e|`$, and define

```math
U_s|a,b\rangle=|a,b+a\cdot s\rangle,\qquad
\tau_\nu=\sum_z\nu(z)Z_z|+\rangle\langle+|Z_z^\dagger.
```

The diagonal phase operations commute with $`U_s`$, so

```math
\rho_s^\nu=U_s(\tau_\nu\otimes\mathrm{diag}\,\chi)U_s^\dagger.
```

The vectors $`Z_z|+\rangle`$ form an orthonormal Fourier basis. This immediately exposes the source spectrum and isolates the encoded information from the noise spectrum. It also explains why a known equivalence before encoding need not give a known conversion after the secret-dependent encoding.

## What is matched, and what is not implied

The marginal statement concerns proper subsets of the **$`n`$ noisy input registers**. The source reductions agree whenever at least one input register is discarded, even if $`B`$ is retained. It does not assert equality for every proper subset of all $`n+1`$ registers: discarding only $`B`$ is a different operation.

Matching the spectrum of each secret-conditioned state does not imply matching the ensemble-average state, Holevo information, or many-copy identifiability. The channels' superoperator spectra are also different. These distinctions are part of the result, with explicit counterexamples and operational interpretation in [Interpretation](interpretation.md).

## Proof dependencies

| Result | Authoritative proof | Main ingredients |
|---|---|---|
| Marginals and matched channel/source diagnostics | [channels.md](channels.md) | Permutation graphs, Schur multipliers, Fourier orthogonality, generalized dephasing |
| Classical-input LWE equivalence | [hardness.md](hardness.md) | Linear coordinate change, exact state simulation, quotient recovery |
| Cubic recovery and fixed-copy bound | [learning.md](learning.md) | Positive Fourier transform, polynomial expansion, finite-field zero bound |
| Fragility and physical resources | [implementation.md](implementation.md) | Full-support Fourier correlations, local dephasing, trace-distance hybrid |
| Information and access boundaries | [interpretation.md](interpretation.md) | Ensemble entropy, commutative limit, source-access comparison |
| Attribution and unresolved comparison | [related work](../references/RELATED_WORK.md) | Primary-source comparison and explicit access limits |

The [finite verification suite](../verification/README.md) checks consequential identities and counterexamples independently of the prose proofs. It does not establish asymptotic hardness or priority.
