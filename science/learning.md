# Secret recovery from cubic phase noise

The cubic phase-noise family leaves an exact polynomial relation in a product Fourier measurement. Lifting that relation to linear features recovers the full secret from a fixed number of independent source copies. This page gives the algorithm, its raw-copy failure bound, and a version that also learns fixed unknown cubic coefficients.

The [source model](model.md) fixes the information supplied to the learner. The [channel comparison](channels.md) proves that the cubic and linear sources have identical classical diagonals, spectra, and every proper-coordinate noise marginal. The linear source's [LWE reduction](hardness.md) supplies the conditional computational contrast.

## Fourier readout

Let $`q>3`$ be prime, $`n\ge2`$, and $`\omega=e^{2\pi i/q}`$. With the positive Fourier convention

```math
F_q|j\rangle=\frac1{\sqrt q}\sum_{k\in\mathbb F_q}\omega^{jk}|k\rangle,
```

a source branch with additive error $`e`$ and phase label $`z`$ transforms as

```math
(F_q^{\otimes n}\otimes F_q)Z_z|\psi_{s,e}\rangle
=\frac1{\sqrt q}\sum_{k\in\mathbb F_q}
\omega^{ke}|-ks-z,k\rangle.
```

Consequently a measurement returns

```math
k\sim\operatorname{Unif}(\mathbb F_q),\qquad
u=-ks-z,\qquad z\sim\nu,
```

with $`k`$ and $`z`$ independent. The additive error law $`\chi`$ drops out of these measurement probabilities. It remains part of the full source density operator and of its classical diagonal.

Fourier extraction from noisy examples follows the line of work of [Cross, Smith and Smolin](https://arxiv.org/abs/1407.5088) and [Grilo, Kerenidis and Zijlstra](https://arxiv.org/abs/1702.08255). The latter's independently noisy example model must not be substituted for this source's shared-per-call error convention. Polynomial graph learning also has established precedents, including [Decker and Wocjan](https://arxiv.org/abs/quant-ph/0703195). The [related-work account](../references/RELATED_WORK.md) identifies what is inherited and what is specific to the matched-channel comparison.

## Theorem: a fixed raw-copy budget

Let $`q\equiv2\pmod3`$ and let $`\nu_C`$ be uniform on

```math
C=\left\{(x_1,\ldots,x_{n-1},\sum_{i=1}^{n-1}x_i^3)
:x_i\in\mathbb F_q\right\}.
```

For any fixed secret $`s\in\mathbb F_q^n`$, any additive error law $`\chi`$, and any $`0<\delta<1`$, the algorithm below recovers $`s`$ with probability at least $`1-\delta`$ using exactly

```math
N=\left\lceil
\frac{2n\ln q+\ln(1/\delta)}{\ln(q/3)}
\right\rceil
```

raw source copies. Copies whose measured $`k`$ is zero are included in this budget. Quantum and classical running times are polynomial in $`n`$, $`\log q`$, and $`\log(1/\delta)`$, with the finite-precision allowance stated below. The learner needs no coherent memory across copies, source inverse, or QRAM.

The condition $`q\equiv2\pmod3`$ ensures the matched local marginals of the channel construction. The recovery calculation and its rank proof themselves only require a prime $`q>3`$.

### The exact polynomial relation

Write $`u'=(u_1,\ldots,u_{n-1})`$ and $`s'=(s_1,\ldots,s_{n-1})`$. A cubic phase label has $`z=(x,\sum_i x_i^3)`$. Since $`x=-u'-ks'`$,

```math
u_n=-ks_n-\sum_i x_i^3
    =-ks_n+\sum_i(u_i+ks_i)^3.
```

For $`k\ne0`$, compute the finite-field response

```math
b=\frac{u_n-\sum_i u_i^3}{k}.
```

Expanding the cubes gives

```math
b=3\sum_i s_i u_i^2
  +3k\sum_i s_i^2u_i
  +k^2\sum_i s_i^3-s_n.
```

Introduce $`D=2n`$ unknowns

```math
\theta=
(s_1,\ldots,s_{n-1},
 s_1^2,\ldots,s_{n-1}^2,
 \sum_i s_i^3,s_n)
```

and the feature row

```math
f(u',k)=
(3u_1^2,\ldots,3u_{n-1}^2,
 3ku_1,\ldots,3ku_{n-1},
 k^2,-1).
```

Each accepted outcome satisfies $`f(u',k)\cdot\theta=b`$ exactly. Conditional on any $`k`$, the vector $`u'=-ks'-x`$ is uniform in $`\mathbb F_q^{n-1}`$, independently of $`k`$. The feature distribution therefore does not depend on the unknown secret.

### Algorithm

1. Request exactly $`N`$ independent source copies. Fourier-transform every input register and the scalar output, then immediately measure them to obtain $`(u,k)`$.
2. When $`k=0`$, keep no regression row. Otherwise compute $`b`$ and $`f(u',k)`$ using exact arithmetic modulo $`q`$.
3. Solve the resulting linear system by Gaussian elimination. If its column rank is below $`2n`$, report failure.
4. Read $`s_1,\ldots,s_{n-1},s_n`$ from the unique solution. The squared entries and cubic sum provide consistency checks; under the promised model they agree automatically.

The extra lifted coordinates are mathematical variables used by the classical solver. They are not additional unknown source parameters or additional quantum registers.

## Proof of the copy bound

We use a product-grid polynomial bound. If a nonzero polynomial has total degree at most $`d`$ and its independent variables are uniform on finite sets of size at least $`M`$, then

```math
\Pr[P=0]\le\frac dM.
```

For completeness, expand in the final variable with highest degree $`j`$. The leading coefficient is a nonzero polynomial of total degree at most $`d-j`$ in the other variables. By induction, it vanishes with probability at most $`(d-j)/M`$. Otherwise the remaining univariate polynomial has at most $`j`$ roots, contributing at most $`j/M`$. Adding the two bounds proves the claim. This is the standard polynomial identity bound; no distributional or computational assumption is needed.

For every nonzero coefficient vector $`\lambda\in\mathbb F_q^{D}`$, the polynomial $`\lambda\cdot f`$ is nonzero: its features are distinct monomials, and $`3\ne0`$ in the field. Its total degree is at most two. Conditional on $`k\ne0`$, the input sets have sizes $`q`$ for each $`u_i`$ and $`q-1`$ for $`k`$. Thus

```math
\Pr[\lambda\cdot f(u',k)=0\mid k\ne0]
\le\frac2{q-1}.
```

A raw copy either has $`k=0`$ and supplies no row, or supplies a row. Its probability of failing to constrain this fixed $`\lambda`$ is at most

```math
\frac1q+\frac{q-1}{q}\frac2{q-1}=\frac3q.
```

If the final feature matrix has column rank below $`D`$, some nonzero $`\lambda`$ lies in its right kernel. Independence of the raw copies and a union bound give

```math
\Pr[\operatorname{rank}<D]
\le(q^D-1)\left(\frac3q\right)^N
<q^D\left(\frac3q\right)^N.
```

The stated choice of $`N`$ makes the last quantity at most $`\delta`$. Because $`q\ge5`$, the denominator $`\ln(q/3)`$ is positive. Moreover,

```math
\frac{\ln q}{\ln(q/3)}
\le\frac{\ln5}{\ln(5/3)},\qquad
\frac1{\ln(q/3)}\le\frac1{\ln(5/3)},
```

so this is uniformly $`O(n+\ln(1/\delta))`$ raw copies over the allowed fields. A full-rank system has the true lifted vector as its unique solution, proving recovery.

## Fixed unknown coefficients

The source need not have perfectly known, unit cubic coefficients. Consider instead uniform phase labels on

```math
C_{c,d_0}
=\left\{(x_1,\ldots,x_{n-1},
d_0+\sum_i c_i x_i^3):x_i\in\mathbb F_q\right\},
```

where $`c_1,\ldots,c_{n-1}\in\mathbb F_q^*`$ and $`d_0\in\mathbb F_q`$ are fixed across calls but unknown to the learner. These constants are independent source parameters; they are not drawn afresh on each copy.

Every proper-coordinate noise marginal remains uniform. Projection onto the first $`n-1`$ coordinates is bijective by the graph definition. If a different coordinate is omitted, fixing the retained coordinates leaves one equation $`c_jx_j^3=t`$ for the missing coordinate. Since $`c_j\ne0`$ and cubing is bijective when $`q\equiv2\pmod3`$, this equation has exactly one solution. All projections onto $`n-1`$ coordinates are therefore bijective, and their smaller marginals are uniform as well. The support still has size $`q^{n-1}`$, so the spectrum and environment counts in [the channel comparison](channels.md) also remain unchanged.

**Theorem.** The secret, all $`c_i`$, and $`d_0`$ can be recovered with failure probability at most $`\delta`$ from the fixed raw-copy budget

```math
N_{\mathrm{cal}}=
\left\lceil
\frac{3n\ln q+\ln(1/\delta)}{\ln(q/3)}
\right\rceil.
```

Here every raw Fourier outcome, including $`k=0`$, contributes a row.

To prove this, expand the unnormalized output relation:

```math
u_n=
\sum_i c_i u_i^3
+3k\sum_i c_i s_i u_i^2
+3k^2\sum_i c_i s_i^2u_i
+k^3\sum_i c_i s_i^3
-ks_n-d_0.
```

Use the $`3n`$ features

```math
g(u',k)=
(u_i^3)_{i<n}\ \oplus
(3ku_i^2)_{i<n}\ \oplus
(3k^2u_i)_{i<n}\ \oplus
(k^3,-k,-1)
```

and unknown vector

```math
\vartheta=
(c_i)_{i<n}\ \oplus
(c_i s_i)_{i<n}\ \oplus
(c_i s_i^2)_{i<n}\ \oplus
\left(\sum_i c_i s_i^3,s_n,d_0\right).
```

The response is simply $`u_n`$. The variables $`u'`$ and $`k`$ are independent and uniform on the full grid $`\mathbb F_q^{n-1}\times\mathbb F_q`$. A nonzero linear combination of the distinct features is a nonzero polynomial of total degree at most three, so it vanishes with probability at most $`3/q`$. The same union-bound proof, now with $`D=3n`$, establishes the stated budget.

The recovered nonzero coefficients give $`s_i=(c_i s_i)/c_i`$ for $`i<n`$, and the lifted vector directly gives $`s_n`$ and $`d_0`$. All other recovered entries can be checked for consistency. This proves the extension without an additional source interface or a separate calibration oracle.

This result concerns fixed unknown coefficients and a fixed offset. It does not cover coefficients fluctuating between calls, independently varying branch errors, or arbitrary phase jitter.

## Cost and finite precision

For the principal learner, each raw outcome contains $`n+1`$ field elements. Feature generation uses $`O(n)`$ field operations per accepted copy. Gaussian elimination on $`O(N)`$ rows and $`2n`$ columns uses $`O(Nn^2)`$ field operations by a straightforward implementation, with $`O(Nn\log q)`$ bits of storage. The coefficient-learning extension has the same polynomial orders with $`3n`$ columns. All divisions are by explicitly nonzero field elements, and the classical arithmetic can be exact.

The quantum circuit only implements independent $`F_q`$ measurements on the received registers. An arbitrary-modulus Fourier transform is not treated as free hardware: [implementation](implementation.md) gives the binary-encoded readout construction, preparation costs, and work-register accounting.

Let the trace-distance error of each independently prepared copy be at most $`\eta_{\mathrm{prep}}`$, and let the complete implemented readout channel have half-diamond distance at most $`\eta_{\mathrm{read}}`$ from its ideal version. A hybrid bound and contractivity imply that, over the fixed raw-copy budget,

```math
\Pr[\text{failure in the implementation}]
\le\delta+N(\eta_{\mathrm{prep}}+\eta_{\mathrm{read}}).
```

For total target error $`\varepsilon`$, one may set $`\delta=\varepsilon/2`$ in the raw-copy formula and choose the combined per-copy implementation error at most $`\varepsilon/(2N)`$. The same statement holds with $`N_{\mathrm{cal}}`$ for the coefficient-learning extension. Marginal error bounds alone are not sufficient for an arbitrarily correlated multi-copy source; independence, or a suitable uniform conditional per-call guarantee, is required.

This finite-precision allowance is not a constant physical-noise threshold. In fact, the [local-dephasing identity](implementation.md) shows that fixed-strength independent dephasing suppresses the relevant global coherence exponentially in $`n`$ and restores closeness to ordinary classical LWE. Fixed unknown cubic coefficients and independent noise accumulated after preparation have different effects.

## What the algorithm establishes

The cubic source is efficiently learnable under the explicit state-copy model, while the linear source is equivalent to residual LWE under the same modulus and additive-error law. The learner exploits global phase correlations that are absent from every proper-coordinate noise marginal. The computation adds no access to the secret-holder's randomness.

The matched spectra do not imply equal ensemble Holevo information. Likewise, ordinary classical LWE samples do not supply the coherent cubic source: a polynomial-time simulator that produced enough such copies would combine with this learner to solve LWE. [Interpretation](interpretation.md) explains these distinctions and the scope of the comparison.
