# What the separation means

[Science guide](README.md) · [Model](model.md) · [Channel invariants](channels.md)

## Noise correlations determine which constraints survive

Both channels erase all coherence visible to any proper subset of the input registers. Both preserve the same amount of relative entropy of coherence and have the same quantum capacity. Yet the surviving coherence can encode different relations with the secret.

For the linear phase support, Fourier readout gives a linear quotient of the secret. The remaining source is exactly simulatable from lower-dimensional classical LWE. For the cubic support, Fourier readout gives polynomial equations whose coefficients reveal the full secret through linear algebra. The distinction is the algebraic form of the constraints across repeated emissions with the same secret.

This establishes a limitation of a particular collection of channel diagnostics for predicting computational learning performance. It does not establish a new attack on standard lattice-based cryptography. The source is additional coherent access, and both its physical preparation and its access restrictions matter.

## The Fourier measurement has equal single-copy mutual information

Use the positive Fourier convention

```math
F|a\rangle=q^{-1/2}\sum_k\omega^{ka}|k\rangle.
```

For either phase law and every error distribution, the readout is

```math
K\sim U(\mathbb F_q),\qquad U=-Z-KS,\qquad Z\sim\nu.
```

Let the secret $`S`$ be uniform in $`\mathbb F_q^n`$. Conditional on any nonzero $`K`$, the marginal $`U`$ is uniform because multiplication by $`K`$ is invertible. At $`K=0`$, it has entropy $`H(\nu)`$. Hence

```math
\begin{aligned}
H(U,K\mid S)&=\log_2q+H(\nu),\\
H(U,K)&=\log_2q+\frac1qH(\nu)+\left(1-\frac1q\right)n\log_2q,\\
I(S;U,K)&=\left(1-\frac1q\right)\left[n\log_2q-H(\nu)\right].
\end{aligned}
```

For the two graph laws, this is exactly $`(1-1/q)\log_2q`$ bits. Therefore even the actual efficient measurement extracts the same amount of single-copy classical mutual information. This amount does not specify whether constraints from repeated samples identify new secret coordinates or repeatedly reveal the same quotient.

The scalar error is absent from this measurement law because it contributes a phase $`\omega^{Ke}`$ before measurement. It is still present in the complete density operator and must not be discarded from the hardness analysis.

## Equal conditional spectra do not imply equal Holevo information

For an ensemble $`\{q^{-n},\rho_s^\nu\}_s`$, define its Holevo information by

```math
\mathcal X_\nu
=S\left(q^{-n}\sum_s\rho_s^\nu\right)
-q^{-n}\sum_sS(\rho_s^\nu).
```

The second term is fixed by the matched source spectrum. The first need not agree: averaging over the secret depends on how the eigenvectors move with $`s`$.

The verification suite constructs the full density matrices at $`n=2,q=5`$, averages over all 25 secrets, and gives the following counterexamples. Values are rounded to nine decimal places and are in bits.

| Error probabilities on labels 0,1,2,3,4 | Linear phase law | Cubic phase law |
|---|---:|---:|
| (1,0,0,0,0) | 3.788113094 | 3.713729015 |
| (1/2,1/4,0,0,1/4) | 2.557930866 | 2.571656843 |
| (1/5,1/5,1/5,1/5,1/5) | 1.857542476 | 1.857542476 |

The difference can have either sign. These finite examples rule out a general equal-Holevo claim; they do not estimate cryptographic hardness or establish an asymptotic information advantage.

### Uniform errors isolate an information-theoretic limit

For uniform $`\chi`$, Fourier transformation makes every $`\rho_s^\nu`$ diagonal. One way to see this is that its $(k,\ell)$ block contains the characteristic function

```math
\widehat\chi(k-\ell)=\sum_e\chi(e)\omega^{e(k-\ell)}
=\mathbf 1_{\{k=\ell\}}.
```

The full source states then commute, and their Holevo information equals the Fourier-readout mutual information above.

For the linear law, shifting the secret by any $`w\in L`$ leaves the Fourier distribution unchanged: $`Z+Kw`$ remains uniform on $`L`$. These secrets yield identical density operators, even across arbitrarily many copies. Only the quotient modulo $`L`$ is identifiable. The cubic learner still recovers the whole secret.

This is an information-theoretic separation in the uniform-error limit. Uniform errors are not the intended computational LWE regime: ordinary LWE samples then contain no information about the secret.

### Narrow errors can make the hard branch identifiable

Suppose $`\chi`$ is supported on a proper set $`E\subset\mathbb F_q`$ with $`p=|E|/q\lt 1`$. After the linear reduction, consider a wrong residual secret $`u'\ne u`$ in dimension $`r=n-1`$. For a fresh uniform $`x`$, its predicted residual

```math
c-x\cdot u'=e+x\cdot(u-u')
```

is uniform in $`\mathbb F_q`$, because $`x\cdot(u-u')`$ is uniform and independent of $`e`$. It belongs to $`E`$ with probability $`p`$. With $`T`$ independent samples, a union bound gives

```math
\Pr[\text{some wrong secret passes all support checks}]
\le(q^r-1)p^T.
```

Thus

```math
T\ge\frac{r\ln q+\ln(1/\delta)}{\ln(1/p)}
```

suffices for exhaustive enumeration to identify the true secret with probability at least $`1-\delta`$. Its computation can still be exponential in $`r`$. For errors with tails, one must separately bound the probability that any of the $`T`$ true errors leaves the chosen truncation set. This example distinguishes computational hardness from an absence of information.

## A local equivalence before encoding is not a source conversion

Write $`|\widetilde z\rangle=Z_z|+\rangle`$. Let $`h`$ be the inverse of the cube permutation. On each of the first $`n-1`$ registers, define a unitary that maps
$`|\widetilde z_i\rangle\mapsto|\widetilde{h(z_i)}\rangle`$, and leave the last register unchanged. Their tensor product $`V`$ maps the linear pre-encoding state to the cubic one:

```math
V\tau_{\nu_L}V^\dagger=\tau_{\nu_C}.
```

Indeed, a linear support point $`(z',\sum_i z_i)`$ becomes
$`(x',\sum_i x_i^3)`$ with $`x_i=h(z_i)`$.

The received states include the secret-dependent encoding:

```math
\rho_s^{\nu_C}
=U_s(V\otimes I_B)U_s^\dagger\,
\rho_s^{\nu_L}\,
U_s(V^\dagger\otimes I_B)U_s^\dagger.
```

The displayed conversion depends on the unknown secret. The nonlinear Fourier-basis permutation does not generally commute with $`U_s`$. Applying the known $`V`$ directly to an encoded state therefore does not implement this conversion.

Under the LWE hardness assumption, an efficient universal conversion of polynomially many hard-source copies into sufficiently many easy-source copies would contradict the hard-side reduction. In the uniform-error limit, such a same-secret conversion is impossible even without a computational restriction: some hard states are identical while the corresponding easy states are distinguishable.

This pre-encoding state equivalence is different from equivalence of the full channels. [Channel invariants](channels.md) shows that the channel superoperator singular values differ.

## Local invisibility does not prevent global channel discrimination

The channels can be distinguished efficiently with a product preparation $`|+\rangle^{\otimes n}`$, product Fourier measurement, and a joint classical test of whether the observed phase labels obey the linear or cubic relation. The required joint feature can be processed classically; an entangled measurement is unnecessary.

The matching local marginals therefore do not imply a general tomography lower bound, cryptographic concealment of the noise law, or an inability to detect its correlations. They show that measurements and summaries restricted to proper input subsets omit the correlation responsible for this learning difference.

## Independent dephasing destroys the globally supported coherence

Every surviving nontrivial Fourier correlation of either phase law involves every input coordinate. Independent dephasing multiplies these terms by the product $`\eta=\prod_j(1-p_j)`$. The exact result in [Implementation and perturbations](implementation.md) shows that fully dephasing even one input register removes all retained coherence.

At a fixed nonzero rate on every site, the distance from classical LWE falls exponentially in the number of registers. The ideal separation is consequently a statement about a controlled correlated-noise source. It is not a fault-tolerance theorem. The analysis does not establish an efficient decoder at the intermediate scaling $`p=O(\log n/n)`$; inverse-polynomial distance from a classical source alone would not prove recoverability.

## Scope of the contribution

The explicit construction combines established tools: Fourier sampling for quantum examples, finite-field polynomial recovery, classical LWE reductions, and the structure of generalized dephasing channels. The claim developed here is their joint consequence for the two specified channels, including the exact list of matched diagnostics and the negative robustness result.

Many of the spectral and scalar matches follow from one common fact: both phase laws are uniform on supports of the same size. The matching proper marginals follow from their balanced graph projections. The computational substance is the exact residual-LWE simulation on one side and full-secret recovery on the other, under the same source-access contract. The collection of matched diagnostics should be read as consequences of these structural facts.

The [related-work comparison](../references/RELATED_WORK.md) distinguishes these ingredients and records a closely titled accepted conference paper whose full text was not located. That access limit prevents an unqualified priority claim. No ring/module-LWE extension, public-key attack, or experimental realization is established by this construction.
