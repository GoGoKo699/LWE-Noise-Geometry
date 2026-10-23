# Channel geometry and matched physical quantities

The linear and cubic phase laws in [the model](model.md) agree on every proper input subsystem, on the spectra of their source states and Choi states, and on their quantum capacity. Their full channel actions differ. This page proves both parts of that statement and identifies the distinctions that remain available to a global experiment.

The computational consequences are established separately by the [LWE reduction](hardness.md) and the [cubic learning algorithm](learning.md). [Implementation and perturbations](implementation.md) describes finite circuits and additional physical noise; [interpretation](interpretation.md) relates these results without identifying channel capacity with learning complexity.

## 1. Definitions and conventions

Let $`q>3`$ be prime with $`q\equiv2\pmod3`$, let $`n\ge2`$, and set $`r=n-1`$ and $`d=q^n`$. All logarithms in entropies and capacities are base two. Write

```math
\omega=e^{2\pi i/q},\qquad
Z_z|a\rangle=\omega^{z\cdot a}|a\rangle,\qquad
|+\rangle_A=d^{-1/2}\sum_{a\in\mathbb F_q^n}|a\rangle .
```

For a probability distribution $`\nu`$ on $`\mathbb F_q^n`$, define

```math
\mathcal D_\nu(X)=\sum_z\nu(z)Z_zXZ_z^\dagger,
\qquad
\tau_\nu=\mathcal D_\nu(|+\rangle\langle+|).
```

The two distributions of interest are uniform on

```math
L=\left\{\left(x,\sum_{j=1}^{r}x_j\right):x\in\mathbb F_q^r\right\},
\qquad
C=\left\{\left(x,\sum_{j=1}^{r}x_j^3\right):x\in\mathbb F_q^r\right\}.
```

Use $`\nu_L`$ and $`\nu_C`$ for these distributions. Both supports have $`q^r=d/q`$ elements. The cube map is a permutation because $`\gcd(3,q-1)=1`$.

The source with secret $`s`$ and classical error law $`\chi`$ is

```math
\rho_s^\nu
 =U_s\bigl(\tau_\nu\otimes\chi_B\bigr)U_s^\dagger,
\qquad
\chi_B=\sum_e\chi(e)|e\rangle\langle e|,
\qquad
U_s|a,b\rangle=|a,b+a\cdot s\rangle.
```

The phase noise commutes with $`U_s`$. The source definition fixes one shared output offset per copy and supplies only copies to the learner; these access assumptions are detailed in [model.md](model.md).

Let $`\Delta_T`$ denote complete computational-basis dephasing on the input sites in $`T`$. Write $`\Delta_A`$ for all input sites and $`\Delta_{AB}`$ for all source registers.

## 2. Equality of every proper reduced channel

### Proposition 1: uniform proper marginals

For either $`\nu_L`$ or $`\nu_C`$, and every proper subset $`T\subsetneq[n]`$,

```math
\nu_T=\mathrm{Unif}(\mathbb F_q^{|T|}).
```

**Proof.** It suffices to check marginals on $`n-1`$ coordinates. Omitting the last coordinate leaves the independent uniform variables $`x_1,\ldots,x_r`$. If coordinate $`x_j`$ is omitted, any specification of all remaining coordinates has exactly one completion. For $`L`$ it is determined by a linear equation. For $`C`$ it is determined by

```math
x_j^3=z_n-\sum_{i\ne j}x_i^3,
```

which has exactly one solution because cubing is bijective. Every $`(n-1)`$-tuple consequently has probability $`q^{-r}`$. Smaller marginals follow by summation. ∎

More generally, the same argument applies to graphs $`z_n=c+\sum_j f_j(x_j)`$ whenever every $`f_j`$ is a permutation of the field. These support sets are classical orthogonal arrays of strength $`n-1`$. Orthogonal arrays and their quantum-control applications are discussed in [Roetteler and Wocjan](https://arxiv.org/abs/quant-ph/0409135) and the [related-work account](../references/RELATED_WORK.md).

### Proposition 2: reduced-channel identity, including references

For either channel, every $`T\subsetneq[n]`$, every reference system $`R`$, and every joint operator $`X_{AR}`$,

```math
\mathrm{Tr}_{A\setminus T}
 \bigl[(\mathcal D_\nu\otimes\mathrm{id}_R)(X_{AR})\bigr]
 =
(\Delta_T\otimes\mathrm{id}_R)
 \bigl(\mathrm{Tr}_{A\setminus T}X_{AR}\bigr).
```

**Proof.** The phase unitary is a tensor product. Unitary invariance of the partial trace on the discarded sites gives

```math
\mathrm{Tr}_{A\setminus T}(Z_zX_{AR}Z_z^\dagger)
 =
Z_{z_T}
 \bigl(\mathrm{Tr}_{A\setminus T}X_{AR}\bigr)
Z_{z_T}^\dagger.
```

Average over $`z`$, apply Proposition 1, and use uniform phase twirling to obtain $`\Delta_T`$. The reference is untouched throughout. ∎

This is an equality of reduced processes for arbitrary global inputs, not merely an equality of the output marginals for one chosen probe.

### Corollary: the corresponding reduced source is classical

For every proper input subset $`T`$, keeping the entire output register $`B`$,

```math
\mathrm{Tr}_{A\setminus T}\rho_s^{\nu_L}
 =
\mathrm{Tr}_{A\setminus T}\rho_s^{\nu_C}
 =
\mathrm{Tr}_{A\setminus T}\rho_s^{\mathrm{cl}},
```

where

```math
\rho_s^{\mathrm{cl}}
 =
\frac1d\sum_{a,e}\chi(e)
 |a\rangle\langle a|
 \otimes |a\cdot s+e\rangle\langle a\cdot s+e|.
```

To see this, apply Proposition 2 with $`B`$ as the reference to the source before phase noise. Tracing missing input sites equates their bra and ket indices; dephasing retained sites equates all other input indices. The output is then diagonal as well. In particular,

```math
\Delta_A\rho_s^\nu
 =\Delta_{AB}\rho_s^\nu
 =\rho_s^{\mathrm{cl}}
```

for every phase law $`\nu`$.

The subsystem qualification matters. Tracing only $`B`$ while retaining all $`n`$ input sites is not covered by Proposition 2. Nor does the proposition prevent taking product measurements on all input sites and examining their joint outcomes.

## 3. Source spectra, entropy, and coherence

### Proposition 3: spectrum for an arbitrary phase law

The vectors

```math
|\phi_z\rangle=Z_z|+\rangle
```

form an orthonormal basis, since $`\langle\phi_w|\phi_z\rangle=d^{-1}\sum_a\omega^{(z-w)\cdot a}=\mathbf1_{z=w}`$. Thus the eigenvalues of $`\tau_\nu`$ are exactly $`\nu(z)`$, including zeros. Unitary conjugation in the source definition gives the eigenvalues

```math
\mathrm{spec}(\rho_s^\nu)
 =\{\nu(z)\chi(e):z\in\mathbb F_q^n,\ e\in\mathbb F_q\}.
```

They do not depend on the secret. Therefore

```math
S(\rho_s^\nu)=H(\nu)+H(\chi).
```

The eigenvalue distribution of $`\rho_s^{\mathrm{cl}}`$ is $`\chi(e)/d`$, repeated over all $`a`$, so

```math
S(\rho_s^{\mathrm{cl}})=n\log_2q+H(\chi).
```

Relative-entropy coherence in the fixed computational basis is consequently

```math
C_{\mathrm{rel}}(\rho_s^\nu)
 :=S(\Delta_{AB}\rho_s^\nu)-S(\rho_s^\nu)
 =n\log_2q-H(\nu).
```

This is a basis-dependent quantity tied here to the classical LWE interface.

For the two uniform graph laws, the complete source spectra match: every nonzero value $`\chi(e)/q^r`$ occurs $`q^r`$ times. Hence

```math
\begin{aligned}
\mathrm{rank}(\rho_s^\nu)
  &=q^r|\mathrm{supp}\,\chi|,\\
\mathrm{Tr}\bigl[(\rho_s^\nu)^2\bigr]
  &=q^{-r}\sum_e\chi(e)^2,\\
S(\rho_s^\nu)
  &=r\log_2q+H(\chi),\\
C_{\mathrm{rel}}(\rho_s^\nu)
  &=\log_2q.
\end{aligned}
```

All spectral Rényi entropies agree as well.

### Environmental dimension and entropy

A Stinespring isometry for $`\mathcal D_\nu`$ is

```math
V_\nu|a\rangle=|a\rangle|E_a\rangle,
\qquad
|E_a\rangle=\sum_z\sqrt{\nu(z)}\,\omega^{z\cdot a}|z\rangle_E.
```

For an input with uniform computational diagonal, including the present source input, the environmental state is

```math
\frac1d\sum_a|E_a\rangle\langle E_a|
 =\sum_z\nu(z)|z\rangle\langle z|.
```

Its entropy is $`H(\nu)`$. For the graph laws this is $`r\log_2q`$, whereas the surviving source coherence is $`\log_2q`$. These are different quantities.

The minimal environment dimension of the channel is its Kraus rank. As the next section shows, that rank is $`|\mathrm{supp}\,\nu|`$, giving the same minimal dimension $`q^r`$ for both channels. The bath implementation in [implementation.md](implementation.md#2-pairwise-bath-realization) attains it with $`r`$ bath qudits.

## 4. Choi spectra and scalar channel metrics

Use the normalized maximally entangled state

```math
|\Phi_d\rangle=d^{-1/2}\sum_a|a\rangle|a\rangle,
\qquad
J_\nu=(\mathcal D_\nu\otimes\mathrm{id})
       (|\Phi_d\rangle\langle\Phi_d|).
```

Then

```math
J_\nu=\sum_z\nu(z)|\Phi_z\rangle\langle\Phi_z|,
\qquad
|\Phi_z\rangle=(Z_z\otimes I)|\Phi_d\rangle.
```

The states $`|\Phi_z\rangle`$ are orthonormal because $`d^{-1}\mathrm{Tr}(Z_w^\dagger Z_z)=\mathbf1_{w=z}`$. Thus $`J_\nu`$ has nonzero spectrum $`\nu`$ and rank $`|\mathrm{supp}\,\nu|`$. For both graph laws its spectrum is uniform on $`q^r`$ eigenvalues.

### Entanglement and average gate fidelity

Entanglement fidelity at the maximally mixed input is

```math
F_e(I/d,\mathcal D_\nu)
 =\langle\Phi_d|J_\nu|\Phi_d\rangle
 =\nu(0).
```

The average gate fidelity relative to the identity is

```math
F_{\mathrm{avg}}(\mathcal D_\nu,\mathrm{id})
 =\frac{d\,\nu(0)+1}{d+1}.
```

This follows either from the Haar second-moment identity applied to $`|\langle\psi|Z_z|\psi\rangle|^2`$, or from the standard relation between entanglement fidelity and average fidelity proved by [Nielsen](https://arxiv.org/abs/quant-ph/0205035). In both graph laws $`0`$ has probability $`q^{-r}`$, and therefore

```math
F_e=q^{-r},
\qquad
F_{\mathrm{avg}}=\frac{q+1}{q^n+1}.
```

### Unitarity

Define the Fourier multiplier

```math
\widehat\nu(\delta)=\sum_z\nu(z)\omega^{z\cdot\delta}.
```

The matrix units form a Hilbert–Schmidt orthonormal eigenbasis:

```math
\mathcal D_\nu(|a\rangle\langle b|)
 =\widehat\nu(a-b)|a\rangle\langle b|.
```

Every difference $`\delta`$ appears $`d`$ times. Parseval gives

```math
\|\mathcal D_\nu\|_{\mathrm{HS}}^2
 =d\sum_\delta|\widehat\nu(\delta)|^2
 =d^2\sum_z\nu(z)^2.
```

For a trace-preserving unital channel, the identity direction separates from the traceless operator subspace. With the conventional unitarity normalization of [Wallman et al.](https://arxiv.org/abs/1503.07865),

```math
u(\mathcal D_\nu)
 =\frac{d^2\sum_z\nu(z)^2-1}{d^2-1}.
```

For either graph law,

```math
u(\mathcal D_\nu)
 =\frac{q^{n+1}-1}{q^{2n}-1}.
```

The matched scalar quantities can be collected as follows.

| Quantity | Common value |
|---|---|
| Proper reduced input channel on $`T`$ | $`\Delta_T`$ |
| Nonzero normalized Choi eigenvalues | $`q^{-r}`$, repeated $`q^r`$ times |
| Minimal phase-bath dimension | $`q^r`$ |
| Phase-bath entropy for a uniform-diagonal input | $`r\log_2q`$ |
| Source coherence | $`\log_2q`$ |
| Entanglement fidelity at $`I/d`$ | $`q^{-r}`$ |
| Average gate fidelity to identity | $`(q+1)/(q^n+1)`$ |
| Channel unitarity | $`(q^{n+1}-1)/(q^{2n}-1)`$ |
| Unassisted quantum capacity | $`\log_2q`$ qubits per complete channel use |

The capacity entry requires the proof below; it does not follow from Choi isospectrality alone.

## 5. Exact quantum capacity

### Proposition 4: capacity of these phase channels

For any distribution $`\nu`$ on $`\mathbb F_q^n`$,

```math
Q(\mathcal D_\nu)=n\log_2q-H(\nu).
```

Consequently $`Q(\mathcal D_{\nu_L})=Q(\mathcal D_{\nu_C})=\log_2q`$.

**Proof.** The complement of the Stinespring isometry above is

```math
\mathcal D_\nu^c(\rho)
 =\sum_a\rho_{aa}|E_a\rangle\langle E_a|.
```

The output of $`\mathcal D_\nu`$ retains the same computational diagonal as its input. Measuring that diagonal and preparing the associated $`|E_a\rangle`$ therefore maps the channel output to its complement. The channel is degradable.

For degradable channels, quantum capacity equals the maximum single-letter coherent information,

```math
Q(\mathcal D_\nu)
 =\max_\rho I_c(\rho,\mathcal D_\nu),
\qquad
I_c(\rho,\mathcal D_\nu)
 =S(\mathcal D_\nu(\rho))-S(\mathcal D_\nu^c(\rho)).
```

This is the generalized-dephasing case of [Devetak and Shor, Appendix B](https://arxiv.org/pdf/quant-ph/0311131). Coherent information is concave in the input for a degradable channel: after an isometric dilation of the degrading map it becomes a conditional entropy, whose concavity supplies the claim.

Let $`X_t|a\rangle=|a+t\rangle`$. Conjugating an input by any tensor Weyl unitary $`X_tZ_v`$ conjugates the main output by that unitary. On the complement, a shift $`X_t`$ conjugates by the diagonal environmental unitary $`|z\rangle\mapsto\omega^{z\cdot t}|z\rangle`$, and $`Z_v`$ leaves the complement unchanged. Both output entropies, and hence coherent information, are invariant.

Twirling the input over all Weyl unitaries gives $`I/d`$. Concavity and invariance imply

```math
I_c(I/d,\mathcal D_\nu)\ge I_c(\rho,\mathcal D_\nu)
```

for every input $`\rho`$. At $`I/d`$, the channel output is $`I/d`$ and the environment has spectrum $`\nu`$, which proves the formula. ∎

This capacity is measured per use of the entire $`n`$-input phase channel. It describes asymptotic coded quantum communication with optimized inputs. The fixed-source recovery problem in [hardness.md](hardness.md) and [learning.md](learning.md) has a different interface and objective.

## 6. Distinctions not fixed by these matches

### 6.1 The complete channels are separated in diamond norm

For any two phase distributions on this common family of unitaries,

```math
\frac12\|\mathcal D_\nu-\mathcal D_\mu\|_\diamond
 =\frac12\sum_z|\nu(z)-\mu(z)|
 =\mathrm{TV}(\nu,\mu).
```

The triangle inequality gives the upper bound, because every unitary channel has diamond norm one. Sending $`|+\rangle`$ through the difference gives a mixture of the orthogonal states $`|\phi_z\rangle`$, attaining the lower bound. An entangled input is unnecessary.

For the graph laws the intersection consists of the solutions of

```math
\sum_{j=1}^{r}(x_j^3-x_j)=0.
```

This is a nonzero polynomial of total degree three over a field of size greater than three. The polynomial zero bound gives $`|L\cap C|\le3q^{r-1}`$, and hence

```math
\frac12\|\mathcal D_{\nu_L}-\mathcal D_{\nu_C}\|_\diamond
 =1-\frac{|L\cap C|}{q^r}
 \ge1-\frac3q
 \ge\frac25.
```

Preparing $`|+\rangle`$, measuring each site in the Fourier basis, and checking the global support equation distinguishes the channels with constant advantage. All devices in this measurement can be local; the relevant statistic combines all $`n`$ outcomes.

### 6.2 Choi isospectrality is not channel-unitary equivalence

For $`L`$, the Fourier multiplier is

```math
\widehat\nu_L(\delta)=\mathbf1_{\delta\in L^\perp},
\qquad
L^\perp
 =\mathrm{span}\{(-1,\ldots,-1,1)\}.
```

Thus every superoperator singular value is either zero or one.

For $`C`$, no nonzero $`\delta`$ has $`|\widehat\nu_C(\delta)|=1`$. Equality in the triangle inequality for an average of unit-modulus phases would force

```math
\sum_{j=1}^{r}\delta_jx_j+\delta_n\sum_{j=1}^{r}x_j^3
```

to be constant for every $`x`$. Its value at zero is zero. Varying one coordinate at a time gives a degree-at-most-three polynomial vanishing on all $`q>3`$ field elements, so its coefficients vanish: $`\delta_n=0`$ and every $`\delta_j=0`$.

On the other hand, Parseval gives

```math
\sum_\delta|\widehat\nu_C(\delta)|^2=q.
```

Since $`\widehat\nu_C(0)=1`$, some nonzero Fourier coefficient has magnitude strictly between zero and one. The superoperator singular-value multisets therefore differ.

Unitary pre- and post-processing act by Hilbert–Schmidt unitary matrices on the superoperator and preserve its singular values. It follows that no unitaries $`V,W`$ satisfy

```math
\mathcal D_{\nu_C}
 =\mathrm{Ad}_V\circ\mathcal D_{\nu_L}\circ\mathrm{Ad}_W.
```

The distinction also appears in exact noiseless sectors. The linear channel preserves all coherences inside each coset of $`L^\perp`$, giving $`q`$-dimensional decoherence-free subspaces. For the cubic channel, the only fixed matrix units are the diagonal ones. Its equal asymptotic capacity is achieved through coding rather than such an exact noiseless sector.

### 6.3 A local unitary does relate the input phase states

At the level of the one chosen channel input, an efficient product unitary $`V`$ that relabels the first $`r`$ Fourier coordinates by the inverse cube permutation satisfies

```math
\tau_{\nu_C}=V\tau_{\nu_L}V^\dagger.
```

The proof and its consequences for the source interface are given in [interpretation.md](interpretation.md). This state identity does not imply the channel-unitary equivalence excluded above.

## 7. What the comparison establishes

The [linear-source reduction](hardness.md) and [cubic learner](learning.md) give different recovery complexity under a fixed source interface, even after matching the properties proved here. The source states and channels retain globally different coherence patterns; neither the same spectrum nor the same communication capacity removes those differences.

The same all-proper-marginal property also forces a specific physical vulnerability: every surviving offdiagonal input matrix element changes all $`n`$ coordinates. [Independent local dephasing](implementation.md#5-exact-effect-of-independent-local-dephasing) therefore attenuates all of it by a single product factor and can restore a classical LWE source up to negligible distance. That exact fragility statement is part of the scope of the comparison.

Definitions and external results used here are placed in context in [RELATED_WORK.md](../references/RELATED_WORK.md).

