# Implementation, accuracy, and additional dephasing

The source and learner in [model.md](model.md) can be implemented with polynomial-size arithmetic circuits and independently prepared state copies. The correlated phase noise needs no large data-loading oracle. Its physical structure is nevertheless specific: the input qudits share a programmed higher-order phase relation, and all surviving coherence changes every input coordinate.

That structure gives an exact response to independent local dephasing. If each of the $`n`$ input registers is partially dephased, the residual coherent component is multiplied by a product of $`n`$ survival factors. Under constant dephasing strength this component is exponentially small, and the resulting source can be simulated from classical $`n`$-dimensional LWE samples up to negligible distance.

This page separates finite gate-synthesis accuracy from that additional physical channel. It complements the [channel identities](channels.md), the [linear-source hardness reduction](hardness.md), the [cubic learner](learning.md), and the [interpretation](interpretation.md).

## 1. Source preparation without a data-loading oracle

Use the conventions of [model.md](model.md): $`q>3`$ is prime, $`q\equiv2\pmod3`$, $`n\ge2`$, $`r=n-1`$, and $`\ell=\lceil\log_2q\rceil`$. A field element occupies the valid subspace $`\{|0\rangle,\ldots,|q-1\rangle\}`$ of an $`\ell`$-qubit register. Arithmetic circuits can be extended reversibly to the remaining binary basis states.

The source holder knows $`s`$. For each fresh copy:

1. Prepare $`n`$ independent registers in $`|+_q\rangle=q^{-1/2}\sum_{a=0}^{q-1}|a\rangle`$.
2. Sample one $`e\sim\chi`$ classically and initialize the output register to $`|e\rangle`$.
3. Compute $`U_s:|a,b\rangle\mapsto|a,b+a\cdot s\rangle`$ reversibly.
4. Sample independent uniform $`x_1,\ldots,x_r`$. Set $`z=(x,\sum_jx_j)`$ for the linear source or $`z=(x,\sum_jx_j^3)`$ for the cubic source, and apply $`Z_z`$ to the inputs.
5. Discard the source's classical randomness and emit only the input and output registers.

Steps 3 and 4 commute. Fresh randomness is used for each emitted copy. The output offset $`e`$ is shared by every coherent branch in that copy; no table of independent errors indexed by $`a`$ is prepared.

### Uniform field states

Uniform state preparation does not require a Fourier transform of arbitrary modulus. Prepare $`H^{\otimes\ell}|0^\ell\rangle`$, reversibly compare the resulting integer with $`q`$, and measure only the comparison flag. Conditional on acceptance, the register is exactly $`|+_q\rangle`$ in the ideal finite gate model. The acceptance probability is $`q/2^\ell>1/2`$.

A rejected register can be reset and retried independently. Expected work is fewer than two attempts per site. With at most $`R`$ attempts per site, the probability that any of the $`n`$ preparations aborts is at most $`n2^{-R}`$. Choosing $`R=\lceil\log_2(n/\varepsilon_{\mathrm{abort}})\rceil`$ gives a fixed polynomial budget and an explicit abort probability. These acceptance events occur before the secret encoder and do not depend on the secret.

Uniform classical field sampling uses the analogous rejection sampler. The error sampler for $`\chi`$ is an explicit assumption: its running time and any distributional approximation error are included in the source cost.

### Arithmetic and phase gates

The dot product can be accumulated into the output register using controlled modular additions. For each binary bit of $`a_j`$, add the known constant $`2^t s_j\bmod q`$ when that bit is one. There are $`n\ell`$ such additions. Standard reversible adders and comparisons give polynomial cost, for example $`O(n\ell^2)`$ Boolean arithmetic gates with reusable workspace in a straightforward implementation. No operation queries an unknown function supplied to the learner.

Cubing and summing the sampled phase labels takes $`O(n\,\operatorname{poly}(\ell))`$ classical work. For a known label $`z_j`$, the phase gate on a binary-encoded field element factors as

```math
Z_{z_j}|a_j\rangle
 =e^{2\pi i z_j a_j/q}|a_j\rangle,
\qquad
a_j=\sum_{t=0}^{\ell-1}2^t a_{j,t}.
```

It can therefore be implemented with $`\ell`$ single-qubit phase rotations of angles $`2\pi z_j2^t/q`$, restricted to the valid subspace. The noise controller can stream the $`x_j`$ values and keep one modular accumulator for the final phase. It does not store an exponentially large amplitude list or use QRAM.

The source needs $`(n+1)\ell`$ system qubits, polynomial workspace, and $`r\log_2q`$ bits of phase-label entropy per copy. Gate-synthesis accuracy for the rotations is addressed in Section 4.

## 2. Pairwise bath realization

The same phase law admits an explicit dilation by independent finite baths. For $`f(x)=x`$ or $`f(x)=x^3\bmod q`$, define

```math
\mathcal D_{j,f}(\rho)
 =\frac1q\sum_{x\in\mathbb F_q}
   (Z_j^xZ_n^{f(x)})\rho(Z_j^xZ_n^{f(x)})^\dagger.
```

The channels commute, and

```math
\mathcal D_f
 =\mathcal D_{r,f}\circ\cdots\circ\mathcal D_{1,f}
```

is exactly the linear or cubic graph channel. Each factor uses one independent uniform bath symbol, coupled to input site $`j`$ and the common hub $`n`$.

For a coherent dilation, prepare $`r`$ bath qudits in $`|+_q\rangle^{\otimes r}`$. Let

```math
N_j=\sum_{a=0}^{q-1}a|a\rangle\langle a|_{A_j},
\qquad
X_j=\sum_{x=0}^{q-1}x|x\rangle\langle x|_{E_j},
\qquad
f(X_j)=\sum_{x=0}^{q-1}f(x)|x\rangle\langle x|_{E_j}.
```

Here $`X_j`$ is a diagonal bath observable; it is distinct from the shift unitary used in the next section. With $`\hbar=1`$, the Hamiltonian

```math
H_f
 =-\frac{2\pi}{qt_0}
   \sum_{j=1}^{r}
   \left(N_j\otimes X_j+N_n\otimes f(X_j)\right)
```

has commuting two-body terms. At time $`t_0`$ it implements

```math
|a\rangle_A|x\rangle_E
 \longmapsto
\omega^{\,\sum_j a_jx_j+a_n\sum_j f(x_j)}
 |a\rangle_A|x\rangle_E.
```

Discarding the baths gives $`\mathcal D_f`$. Preparing each bath in $`I/q`$ instead gives the same reduced channel through a classical mixture. Entanglement in the initial bath is unnecessary.

The two constructions have the same number and dimension of baths. For the source's uniform input diagonal, the pure dilation leaves the bath uniform on $`q^r`$ orthogonal labels, with entropy $`r\log_2q`$. This attains the minimal channel-environment dimension proved in [channels.md](channels.md#3-source-spectra-entropy-and-coherence). It can be encoded in $`r\ell`$ qubits, using one binary register per bath qudit.

### Locality and interaction strength

These are pairwise system-bath couplings on a star graph. A common input site interacts with all $`r`$ baths; no fixed-dimensional geometric layout or constant circuit depth is assumed. The couplings can be scheduled sequentially in polynomial depth, or their classical phase-kick version can use ordinary classical control and local rotations.

The displayed Hamiltonian also specifies its scale:

```math
\|H_f\|
 \le\frac{4\pi r(q-1)^2}{qt_0}
 <\frac{4\pi rq}{t_0}.
```

Thus a fixed interaction time allows total strength growing polynomially with $`n`$ and $`q`$. Bounding the individual interaction strength instead requires the corresponding increase in duration. Since cubing permutes the field, $`f(X_j)`$ has the same eigenvalue set as $`X_j`$; their correlation with the other bath coupling differs.

This is a finite bath model or an engineered classical phase-noise model. Identifying it with a particular thermal or hardware environment would require an additional physical model.

## 3. Fourier readout with explicit arithmetic

The learner uses the product Fourier measurement described in [learning.md](learning.md). It can be implemented without taking an arbitrary-modulus Fourier transform as a unit-cost primitive.

Define the publicly known modular shift on one field register by

```math
T_q|a\rangle=|a+1\bmod q\rangle.
```

For the positive Fourier convention $`F_q|a\rangle=q^{-1/2}\sum_u\omega^{au}|u\rangle`$, the Fourier-measurement eigenvector for outcome $`u`$ is

```math
|\widetilde u\rangle=F_q^\dagger|u\rangle,
\qquad
T_q|\widetilde u\rangle=\omega^u|\widetilde u\rangle.
```

Measuring the eigenphase of $`T_q`$ and rounding to the nearest multiple of $`1/q`$ therefore implements the desired measurement.

### Phase estimation cost

Use a $`t`$-qubit phase-estimation register with $`N=2^t`$. Every controlled power needed by phase estimation is explicit:

```math
T_q^{2^j}|a\rangle=|a+2^j\bmod q\rangle.
```

It is a controlled addition of a known modular constant. The powers do not require $`2^j`$ calls to an unknown oracle.

For an eigenphase $`\theta=u/q`$, ideal binary phase estimation has output probabilities

```math
p_\theta(y)
 =\frac1{N^2}
   \left|\sum_{v=0}^{N-1}
          e^{2\pi i v(\theta-y/N)}\right|^2.
```

The geometric-series formula bounds the probability outside a circular interval of radius $`1/(2q)`$ around $`\theta`$ by $`O(q/N)`$. A direct tail bound gives at most $`4q/N`$ for $`N\ge4q`$. For example,

```math
t=\left\lceil\log_2\frac{8q}{\varepsilon_{\mathrm{phase}}}\right\rceil
```

is sufficient for a rounded eigenvalue error at most $`\varepsilon_{\mathrm{phase}}`$. To obtain the tail bound, write $`d_y`$ for the circular distance between $`N\theta`$ and $`y`$. The sine denominator gives $`p_\theta(y)\le1/(4d_y^2)`$, and summing over $`d_y\ge N/(2q)`$ bounds the tail.

The controlled additions and the binary inverse Fourier circuit cost

```math
O\!\left(t\,\operatorname{poly}(\ell)+t^2\right)
```

elementary arithmetic and controlled-rotation operations before finite-gate synthesis. The standard phase-estimation construction is described by [Cleve, Ekert, Macchiavello, and Mosca](https://arxiv.org/abs/quant-ph/9708016).

For an arbitrary input, possibly entangled with other registers, discard the measured field register after the procedure. The resulting measurement is the ideal Fourier measurement followed by a classical confusion channel whose error probability is uniformly bounded by $`\varepsilon_{\mathrm{phase}}`$. Its half-diamond distance from ideal readout is therefore at most that error. Applying the procedure to all $`n+1`$ source registers gives readout error at most $`(n+1)\varepsilon_{\mathrm{phase}}`$, before rotation-synthesis error.

The work register can be reused across source registers and copies. The attack requires no quantum memory across independently measured copies; the later regression is classical.

## 4. Preparation and gate approximation

For states, use $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. For channels, use half the diamond norm when reporting operational distance.

### A fixed protocol has an explicit error budget

Suppose an ideal protocol uses at most $`M`$ raw source copies, succeeds with probability at least $`1-\delta_{\mathrm{alg}}`$, and the actual source obeys

```math
\sup_sD(\widetilde\rho_s,\rho_s)\le\varepsilon_{\mathrm{src}}.
```

Assume independent preparation of its copies, and let the implemented readout channel per copy be within half-diamond distance $`\varepsilon_{\mathrm{read}}`$ of ideal readout. A telescoping hybrid and contractivity give

```math
P_{\mathrm{fail}}^{\mathrm{actual}}
 \le
\delta_{\mathrm{alg}}
 +M(\varepsilon_{\mathrm{src}}+\varepsilon_{\mathrm{read}}).
```

The same source bound holds for any collective processing of all $`M`$ copies. Raw-copy budgets are used here so that rejection of outcomes such as $`k=0`$ cannot hide an uncontrolled postselection factor. A fixed-budget learner can include its shortage-of-accepted-samples probability in $`\delta_{\mathrm{alg}}`$, as in [learning.md](learning.md).

If a circuit has $`G`$ ideal unitary gates and each is approximated in operator norm to accuracy $`\gamma_j`$, its half-diamond implementation error is at most $`\sum_j\gamma_j`$. Thus setting each $`\gamma_j\le\varepsilon_{\mathrm{gate}}/G`$ suffices. State-preparation abort probability and classical sampler total-variation errors add to this budget. In particular, changing $`\chi`$ or the phase-label distribution by total variation $`\varepsilon`$ changes a source copy by at most $`\varepsilon`$.

Single-qubit rotations and the controlled rotations in binary phase estimation can be synthesized from a finite universal gate set with overhead polynomial in $`\log(G/\varepsilon_{\mathrm{gate}})`$; [Dawson and Nielsen](https://arxiv.org/abs/quant-ph/0505030) give a constructive Solovay–Kitaev bound. Combined with the arithmetic above, achieving a target total statistical error has polynomial circuit cost per source copy in

```math
n,\quad \log q,\quad \log M,\quad
\log(1/\varepsilon_{\mathrm{total}}),
```

in addition to the cost of the specified error sampler. The complete experiment uses at most $`M`$ times this per-copy quantum cost, followed by classical regression.

For a fixed polynomial-copy learner, inverse-polynomial per-copy error is sufficient when chosen according to its actual $`M`$ and target failure probability. In a hardness reduction quantified over every polynomial-time adversary, simulation error must instead be negligible, or the faulty source must have an exact reduction of its own. Negligible gate-synthesis error is compatible with polynomial overhead when its logarithmic accuracy target is polynomially bounded.

These are compilation and simulation statements in a finite gate model. They do not assume that uncontrolled physical errors can be reduced by gate synthesis.

## 5. Exact effect of independent local dephasing

Let $`\nu`$ be any phase law on $`\mathbb F_q^n`$ whose marginal on every proper coordinate subset is uniform. This includes both graph laws and the fixed permutation-graph variants discussed in [channels.md](channels.md#2-equality-of-every-proper-reduced-channel).

For each entire $`q`$-level input register, define the partial-dephasing channel

```math
\Lambda_{p_j}^{(j)}
 =(1-p_j)\operatorname{id}_{A_j}+p_j\Delta_j,
\qquad
0\le p_j\le1,
\qquad
\eta=\prod_{j=1}^{n}(1-p_j).
```

### Proposition 5: product attenuation identity

For $`n\ge2`$,

```math
\left(\bigotimes_{j=1}^{n}\Lambda_{p_j}^{(j)}\right)
 \circ\mathcal D_\nu
 =
\eta\mathcal D_\nu+(1-\eta)\Delta_A.
```

This is a channel identity and remains valid with any reference system.

**Proof.** On the input matrix unit $`|a\rangle\langle b|`$, the phase channel has multiplier $`\widehat\nu(a-b)`$. If the difference $`\delta=a-b`$ is nonzero but has any zero coordinate, its support is a proper subset. Uniformity of that marginal gives

```math
\widehat\nu(\delta)
 =\mathbb E_{z_{\operatorname{supp}\delta}}
    \omega^{z_{\operatorname{supp}\delta}\cdot
             \delta_{\operatorname{supp}\delta}}
 =0.
```

Every nonzero surviving offdiagonal difference consequently changes all $`n`$ input coordinates. Local partial dephasing multiplies it by $`\prod_j(1-p_j)=\eta`$. Diagonal matrix units are unchanged, and all other offdiagonal units are already zero. This is precisely the action of $`\eta\mathcal D_\nu+(1-\eta)\Delta_A`$. Matrix units span the operator space, proving the identity. ∎

One completely dephased input register makes $`\eta=0`$ and destroys all remaining input coherence, even though the other registers are untouched.

The channel has a standard continuous-time realization. The commuting generators $`\mathcal L_j=\gamma_j(\Delta_j-\operatorname{id})`$ give

```math
e^{t\mathcal L_j}
 =e^{-\gamma_jt}\operatorname{id}
  +(1-e^{-\gamma_jt})\Delta_j,
\qquad
\eta=e^{-t\sum_j\gamma_j}.
```

Here locality refers to complete logical field registers. A binary-encoded hardware device must first identify its physical noise with this logical channel before this exact formula applies.

### Corollary 5.1: exact distance from the classical source

The additionally dephased source is

```math
\sigma_s^{\nu,\eta}
 =
\eta\rho_s^\nu+(1-\eta)\rho_s^{\mathrm{cl}},
```

where $`\rho_s^{\mathrm{cl}}`$ is exactly the computational-basis state of one ordinary classical $`n`$-dimensional LWE sample. Since

```math
\rho_s^\nu
 =U_s(\tau_\nu\otimes\chi_B)U_s^\dagger,
\qquad
\rho_s^{\mathrm{cl}}
 =U_s((I/d)\otimes\chi_B)U_s^\dagger,
```

unitary invariance and the common eigenbasis of $`\tau_\nu`$ and $`I/d`$ give

```math
D(\sigma_s^{\nu,\eta},\rho_s^{\mathrm{cl}})
 =\eta\operatorname{TV}(\nu,U),
\qquad
U=\operatorname{Unif}(\mathbb F_q^n).
```

For either uniform graph law,

```math
\operatorname{TV}(\nu,U)=1-\frac1q,
\qquad
D(\sigma_s^{\nu,\eta},\rho_s^{\mathrm{cl}})
 =\eta\left(1-\frac1q\right).
```

The same value is the half-diamond distance of the additionally dephased phase channel from $`\Delta_A`$, by the phase-channel distance formula in [channels.md](channels.md#61-the-complete-channels-are-separated-in-diamond-norm).

For $`M`$ independent copies,

```math
D\!\left((\sigma_s^{\nu,\eta})^{\otimes M},
         (\rho_s^{\mathrm{cl}})^{\otimes M}\right)
 \le
M\eta\left(1-\frac1q\right).
```

The bound is uniform in the secret and error law.

### Corollary 5.2: a conditional hardness regime

A classical LWE oracle can simulate $`\rho_s^{\mathrm{cl}}`$ exactly: load its sample $`(a,b)`$ into computational basis registers. If a quantum algorithm recovers $`s`$ from $`M`$ additionally dephased source copies with success probability $`\beta`$, the same algorithm on this classical-input simulator succeeds with probability at least

```math
\beta-M\eta\left(1-\frac1q\right).
```

Consequently, when $`\eta`$ is negligible in the security parameter, polynomial-copy recovery from either source remains hard under the corresponding quantum hardness assumption for classical-input $`n`$-dimensional LWE. This includes the cubic source whose ideal version has the learner in [learning.md](learning.md). The dimensional statement here is $`n`$-LWE; the ideal linear source has the separate exact $`(n-1)`$-LWE equivalence in [hardness.md](hardness.md).

Taking $`n`$ as the asymptotic parameter, the exact heterogeneous condition for negligibility is

```math
-\sum_{j=1}^{n}\ln(1-p_j)=\omega(\ln n),
```

with $`p_j=1`$ giving zero immediately. For equal strengths $`p_j=p`$,

```math
\eta=(1-p)^n\le e^{-np}.
```

Every constant $`p>0`$ gives exponential decay. More generally, $`np/\ln n\to\infty`$ is sufficient.

This is an exact fragility result for a specified family of local channels. It does not infer hardness merely because noisy regression resembles LWE; it supplies a simulator and a trace-distance reduction.

## 6. Matched spectra and capacity along the dephasing trajectory

Proposition 5 is also a phase-channel mixture:

```math
\nu_\eta=\eta\nu+(1-\eta)U,
\qquad
\mathcal D_{\nu_\eta}
 =\eta\mathcal D_\nu+(1-\eta)\Delta_A.
```

For a uniform graph support of size $`d/q`$,

```math
\nu_\eta(z)=
\begin{cases}
[1+(q-1)\eta]/d,&z\text{ lies in the graph},\\
(1-\eta)/d,&z\text{ lies outside the graph}.
\end{cases}
```

The two broadened phase laws therefore retain identical probability multisets. Their source spectra, Choi spectra, bath entropies, coherence, fidelity metrics, and unitarity remain matched at every common $`\eta`$. Every proper coordinate marginal stays uniform. Their capacities are equal, but are generally smaller than the ideal value $`\log_2q`$.

Set

```math
\alpha=\frac{1+(q-1)\eta}{q}.
```

The general capacity and coherence formulas in [channels.md](channels.md#5-exact-quantum-capacity) give

```math
\begin{aligned}
Q(\mathcal D_{\nu_\eta})
 &=C_{\mathrm{rel}}(\sigma_s^{\nu,\eta})\\
 &=\log_2q-h_2(\alpha)-(1-\alpha)\log_2(q-1)\\
 &=\frac{1+(q-1)\eta}{q}
      \log_2[1+(q-1)\eta]
   +\frac{(q-1)(1-\eta)}q\log_2(1-\eta),
\end{aligned}
```

with the convention $`0\log_2 0=0`$. This interpolates from $`\log_2q`$ at $`\eta=1`$ to zero at $`\eta=0`$.

The expression is the classical relative entropy $`D_{\mathrm{KL}}(\nu_\eta\|U)`$. Jensen's inequality gives its upper bound by order-two relative entropy:

```math
\begin{aligned}
Q(\mathcal D_{\nu_\eta})
 &\le
 \log_2\!\left(d\sum_z\nu_\eta(z)^2\right)\\
 &=\log_2[1+(q-1)\eta^2]\\
 &\le\frac{(q-1)\eta^2}{\ln2}.
\end{aligned}
```

For polynomially bounded $`q`$ and constant $`p>0`$, both quantum capacity and source coherence therefore decay exponentially with $`n`$. This describes the particular dephasing trajectory, not a statement that the ideal channels have vanishing capacity.

The distance between the two complete channels also contracts exactly:

```math
\frac12\|\mathcal D_{\nu_{L,\eta}}
           -\mathcal D_{\nu_{C,\eta}}\|_\diamond
 =
\eta\,\operatorname{TV}(\nu_L,\nu_C).
```

## 7. Perturbative success and the regime not settled here

The same hybrid method gives a small-noise guarantee for the ideal cubic learner. For either graph law,

```math
D(\sigma_s^{\nu,\eta},\rho_s^\nu)
 =(1-\eta)\left(1-\frac1q\right).
```

A learner using at most $`M`$ raw copies therefore loses at most $`M(1-\eta)(1-1/q)`$ in success probability. For equal small local strengths, $`1-\eta\le np`$, so $`p=O(\delta/(Mn))`$ is a sufficient perturbative scale for success loss $`O(\delta)`$. This is a conservative sufficient condition, not an optimized noise threshold.

Between this regime and negligible $`\eta`$, neither the simulator bound nor the exact interpolation algorithm classifies the optimal recovery complexity. In particular, the formulas do not supply a generic constant-noise-tolerant cubic learner.

There is a separate distinction between fixed calibration parameters and fresh noise. [The fixed-unknown-coefficients extension](learning.md#fixed-unknown-coefficients) learns constant nonzero cubic coefficients and a constant offset jointly with the secret. If an independent extra phase label $`\xi`$ is instead added to the hub on each copy, then

```math
z_n=\sum_jz_j^3+\xi,
\qquad
u_n=-ks_n+\sum_j(u_j+ks_j)^3-\xi.
```

The polynomial relation acquires a fresh error term. Exact regression no longer applies. Without an additional reduction or decoding argument, this observation alone establishes neither hardness nor an efficient robust learner. Uniform hub dephasing is covered exactly by Proposition 5 and makes the source fully classical.

The external ingredients for finite circuits, channel capacity, and noise characterization are catalogued in [RELATED_WORK.md](../references/RELATED_WORK.md). The physical and computational conclusions above follow from the stated source interface and channel equations; they do not require an uncharged state-preparation oracle.

