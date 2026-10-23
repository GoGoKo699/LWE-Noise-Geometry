# Residual lattice hardness

Complete dephasing of a rank-$`r`$ linear record leaves exactly the difficulty of classical-input, $`r`$-dimensional learning with errors (LWE). The remaining coherent directions reveal the complementary part of the secret. This page proves both reductions and specializes them to the linear phase-noise family used in the comparison.

The [source model](model.md) fixes independent state-copy access, the error convention, and Fourier signs. The [channel comparison](channels.md) establishes the matched spectra and local noise marginals. The efficient learner for the cubic family is in [secret recovery](learning.md).

## The classical problem and its assumption

For a prime $`q`$, an error distribution $`\chi`$ on $`\mathbb F_q`$, and a fixed uniformly random secret $`u\in\mathbb F_q^r`$, classical-input search LWE supplies independent pairs

```math
(x,c),\qquad
x\sim\mathrm{Unif}(\mathbb F_q^r),\qquad
c=x\cdot u+e,\qquad e\sim\chi.
```

The task is to recover $`u`$. A quantum algorithm may process these classical samples arbitrarily; the input does not include a coherent sampler, its inverse, or reusable randomness. The hardness assumption used here is that no quantum polynomial-time algorithm recovers the uniform secret with nonnegligible probability from polynomially many samples in the chosen asymptotic parameter family.

This is a computational assumption. Regev's [lattice-to-LWE reduction](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) supplies its standard worst-case lattice motivation for appropriate Gaussian errors. The results below do not prove that assumption, estimate concrete security bits, or assert hardness for every error distribution. The [related-work account](../references/RELATED_WORK.md) distinguishes this inherited assumption from the quantum-source comparison.

## Theorem: a fixed linear record

Let $`W\subseteq\mathbb F_q^n`$ be a known linear subspace of dimension $`r`$, and let $`\nu_W`$ be its uniform distribution. Use the source

```math
\rho_s^{\nu_W}
=\mathcal D_{\nu_W}
  \left(\sum_{e\in\mathbb F_q}\chi(e)
  |\psi_{s,e}\rangle\langle\psi_{s,e}|\right),
\qquad
|\psi_{s,e}\rangle
=q^{-n/2}\sum_{a\in\mathbb F_q^n}|a,a\cdot s+e\rangle,
```

where $`s`$ is uniformly random and each source call draws a fresh $`e`$ shared across that call's coherent branches. The phase operator convention is $`Z_z|a\rangle=\omega^{z\cdot a}|a\rangle`$, with $`\omega=e^{2\pi i/q}`$.

Full-secret recovery from these quantum copies is polynomial-time equivalent to classical-input $`r`$-dimensional search LWE with the same $`q`$ and $`\chi`$.

- A quantum-source learner using $`m`$ copies can be simulated using exactly $`m`$ classical $`r`$-dimensional LWE samples and polynomial overhead. The resulting LWE solver succeeds with at least the learner's full-secret success probability.
- An $`r`$-dimensional LWE solver using $`m`$ samples gives a quantum-source learner using $`m+\ell`$ copies, with an additional failure probability at most $`q^{-\ell}`$. If $`r=n`$, there is no complementary secret to learn and the extra copies are unnecessary.

These are exact reductions in the ideal finite-dimensional model. [Implementation](implementation.md) accounts for finite-precision preparation and readout. The case $`r=0`$ means an empty residual LWE problem.

### The record and its coordinates

Choose a full-row-rank matrix $`B\in\mathbb F_q^{r\times n}`$ with row space $`W`$. Averaging the phases gives

```math
\mathcal D_{\nu_W}(|a\rangle\langle a'|)
=\mathbf 1\{B(a-a')=0\}|a\rangle\langle a'|.
```

Thus this channel is exactly the operation that writes $`Ba`$ into an environment and discards that environment. It preserves coherence within each fiber of the linear record.

Let $`d=n-r`$. Choose an invertible matrix $`T`$ satisfying

```math
BT=[I_r\ \ 0],\qquad
a=T\binom{x}{y},\qquad
T^{\mathsf T}s=\binom{u}{v},
```

with $`x,u\in\mathbb F_q^r`$ and $`y,v\in\mathbb F_q^d`$. A right inverse of $`B`$ supplies the first $`r`$ columns of $`T`$; a basis of $`\ker B`$ supplies the remaining columns. Gaussian elimination constructs this coordinate change in polynomial time.

The bilinear form becomes $`a\cdot s=x\cdot u+y\cdot v`$. After the reversible coordinate change, a source copy is

```math
\frac1{q^r}\sum_{x,e}\chi(e)
|x\rangle\langle x|\otimes
|\phi_{v,x\cdot u+e}\rangle
\langle\phi_{v,x\cdot u+e}|,
```

where

```math
|\phi_{v,c}\rangle
=q^{-d/2}\sum_{y\in\mathbb F_q^d}|y,c+y\cdot v\rangle.
```

The record $`x`$ is classical; the coherent fiber contains the complementary secret $`v`$.

### Learning the complementary secret

Apply the positive Fourier transform to $`y`$ and the scalar output. For every $`c`$,

```math
(F_q^{\otimes d}\otimes F_q)|\phi_{v,c}\rangle
=\frac1{\sqrt q}\sum_{k\in\mathbb F_q}
\omega^{kc}|-kv,k\rangle.
```

The measured label $`k`$ is uniform. Whenever $`k\ne0`$, the first register determines $`v`$ exactly by multiplication by $`-k^{-1}`$. This event has probability $`1-1/q`$ independently of $`x,u,e`$, and $`\chi`$. All $`\ell`$ attempts fail with probability $`q^{-\ell}`$.

Once $`v`$ is known, subtract $`y\cdot v`$ from the scalar output of a fresh copy. Up to reordering the registers, the resulting density operator is exactly

```math
\left[
\frac1{q^r}\sum_{x,e}\chi(e)
|x,x\cdot u+e\rangle\langle x,x\cdot u+e|
\right]
\otimes |+_q^{\otimes d}\rangle\langle+_q^{\otimes d}|.
```

The bracket is one ordinary $`r`$-dimensional LWE sample. The other register is a known pure state independent of the residual secret. Applying the LWE solver to fresh samples and then computing $`s=T^{-\mathsf T}(u,v)`$ proves one direction.

### Simulating quantum copies from classical LWE

For the converse, suppose a classical LWE oracle has an unknown uniform secret $`u\in\mathbb F_q^r`$. Choose an independent uniform vector $`v\in\mathbb F_q^d`$ and retain its value. For each classical pair $`(x,c)`$, prepare

```math
|x\rangle\otimes
q^{-d/2}\sum_y|y,c+y\cdot v\rangle,
```

and apply the reversible map $`(x,y)\mapsto T(x,y)`$ to the input register. Averaging the classical pair gives precisely one copy of $`\rho_s^{\nu_W}`$, with

```math
s=T^{-\mathsf T}\binom{u}{v}.
```

This secret is uniform in $`\mathbb F_q^n`$. Independent classical samples produce independent quantum copies with that same secret. A learner that recovers $`s`$ therefore recovers $`u`$ by applying $`T^{\mathsf T}`$ and taking its first $`r`$ entries.

The simulator prepares a uniform fiber and computes a known modular dot product. It does not load a stored sample table into superposition, query an unknown LWE secret coherently, or reuse an error across multiple classical samples. This proves the claimed sample-preserving hardness reduction against arbitrary quantum processing of the copies.

## The linear family in the comparison

The [matched channel construction](channels.md) uses

```math
L=\left\{(z_1,\ldots,z_{n-1},\sum_{i=1}^{n-1}z_i)
:z_i\in\mathbb F_q\right\}.
```

Its dimension is $`n-1`$, and its orthogonal complement is spanned by $`(-1,\ldots,-1,1)`$. The canonical coordinates have an especially simple form:

```math
x_i=a_i+a_n\quad(1\le i<n),\qquad y=a_n,
```

so that

```math
a\cdot s
=\sum_{i=1}^{n-1}x_i s_i+y\kappa,
\qquad
\kappa=s_n-\sum_{i=1}^{n-1}s_i.
```

The source reveals $`\kappa`$ through the coherent fiber. Subtracting $`\kappa y`$ from a fresh output leaves classical LWE for $`(s_1,\ldots,s_{n-1})`$. Conversely, one such classical sample $`(x,c)`$, together with a chosen known uniform $`\kappa`$, prepares

```math
\frac1{\sqrt q}\sum_{y\in\mathbb F_q}
|x_1-y,\ldots,x_{n-1}-y,y\rangle|c+\kappa y\rangle.
```

The full secret has $`s_n=\kappa+\sum_{i<n}s_i`$. This is the exact $`(n-1)`$-dimensional LWE reduction used by the principal separation; it changes neither the modulus nor the error distribution.

## A fixed unknown record can be identified

Knowledge of the fixed record subspace is not a hidden source of hardness. Fourier-transforming all registers of the rank-$`r`$ source gives

```math
u_{\mathrm{out}}=-ks-z,
\qquad k\sim\mathrm{Unif}(\mathbb F_q),
\qquad z\sim\mathrm{Unif}(W).
```

Conditioning on $`k\ne0`$, the normalized vector $`w=-u_{\mathrm{out}}/k`$ is uniform on the affine subspace $`s+W`$. After one such vector $`w_0`$, differences of subsequent vectors from $`w_0`$ are independent uniform samples from $`W`$, conditional on $`w_0`$.

With $`m=r+t`$ differences, the probability that they fail to span $`W`$ is bounded by

```math
\Pr[\text{incomplete span}]
\le\sum_{j=0}^{r-1}q^{j-m}
<\frac{q^{-t}}{q-1}.
```

If $`r`$ is unknown, use $`m=n+t`$. Gaussian elimination then identifies $`W`$ and the representative $`s_0=w_0\in s+W`$. For a basis matrix $`C`$ of $`W`$, write $`s=s_0+C\tau`$. Computational-basis samples satisfy

```math
b-a\cdot s_0=(C^{\mathsf T}a)\cdot\tau+e.
```

Because $`C^{\mathsf T}`$ has rank $`r`$, its image of uniform $`a`$ is uniform in $`\mathbb F_q^r`$. These are again exact residual LWE samples. This statement concerns one fixed subspace; it does not assume a secret-dependent or changing record process.

## An asymptotic lattice regime

The algebraic reductions hold for every prime $`q`$ and every $`\chi`$. The cubic comparison additionally uses $`q>3`$ and $`q\equiv2\pmod3`$. To interpret the linear family as a lattice-hard family, select parameters satisfying a stated LWE hardness assumption rather than keeping $`q`$ fixed in an asymptotic lattice claim.

For example, consider admissible primes $`q=\Theta(n^2)`$ and Regev's rounded Gaussian law $`\overline\Psi_\alpha`$ with $`\alpha=1/n`$. At residual dimension $`r=n-1`$, the condition $`\alpha q>2\sqrt r`$ holds for sufficiently large $`n`$. Regev's theorem then connects efficient LWE recovery to worst-case quantum lattice approximation within $`\widetilde O(r/\alpha)=\widetilde O(n^2)`$. This gives a concrete polynomial-parameter regime for the conditional comparison. It does not establish a numerical security level or recommend cryptosystem parameters. See [Regev's theorem and definitions](https://cims.nyu.edu/~regev/papers/qcrypto.pdf).

The small fields used in [verification](../verification/README.md) check finite algebra and density operators. They do not test asymptotic LWE hardness.

## Boundaries of the reduction

The rank theorem is an equivalence for every error law, but its hardness interpretation requires the chosen law to make classical LWE hard. With noiseless errors, classical linear algebra recovers the residual secret. With uniform errors, the residual secret is information-theoretically hidden. Neither endpoint is the usual narrow-error lattice-hardness claim.

For ordinary narrow errors, the residual secret can be identifiable from polynomially many classical samples while exhaustive recovery takes large computation. The comparison therefore does not rely on an absence of classical statistical information. Equal per-secret spectra also do not imply equal ensemble Holevo information; [interpretation](interpretation.md) states precisely which information quantities are matched.

The source gives one independently randomized state per call. If a different interface allowed several chosen inputs under the same additive error, subtracting its evaluations would reveal the secret classically. No such interface is included. Independently choosing a separate error $`e_a`$ for every coherent branch is also a different source model: the exact fiber simulation above does not cover it.

Finally, the principal hard family reduces to $`(n-1)`$-dimensional LWE. The [additional local-dephasing result](implementation.md) concerns closeness to fully classical, $`n`$-dimensional LWE and invokes that separate assumption when making a computational conclusion. Neither result supplies an attack on an ordinary lattice public key.
