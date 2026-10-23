# Watrous bridge

[Learning guide](README.md) · [Milestones](MILESTONES.md) · [Scientific account](../science/README.md)

Watrous supplies the language for states, channels, measurements, and information. This project uses that language to ask which equations about an unknown secret survive correlated phase noise. The bridge below identifies the useful book sections, translates conventions, and follows one small example from a noise distribution to a recovered secret. The general proofs remain in the scientific account.

The selected book is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**, DOI [10.1017/9781316848142](https://doi.org/10.1017/9781316848142), bibliography key `watrous2018`. The [author's book page](https://jhwatrous.github.io/books-and-courses.html) links a [2018 prepublication manuscript](https://jhwatrous.github.io/TQI.pdf). Section pointers below were checked against that manuscript; it is distinct from the published edition. Use section numbers rather than transferring PDF page numbers between versions.

## Focused reading route

| Purpose | Watrous sections | Project connection | Milestones |
|---|---|---|---|
| Describe the emitted object and its readout | §§2.1–2.3; emphasize §2.2.2 | [Source contract](../science/model.md#access-contract), representations, and measurement probabilities | [M01–M05](MILESTONES.md#m01) |
| Recognize the phase channel in several forms | §§4.1.1–4.1.3; §4.2.2 | [Channel action](../science/channels.md): random unitaries, tensor Weyl covariance, entrywise multipliers | [M06](MILESTONES.md#m06), [M16–M17](MILESTONES.md#m16) |
| Separate spectrum from information about the secret | §§5.1.1, 5.2.1–5.2.2; §5.3.3 | [Source entropy](../science/channels.md#3-source-spectra-entropy-and-coherence) and [ensemble distinctions](../science/interpretation.md) | [M08–M09](MILESTONES.md#m08), [M11](MILESTONES.md#m11), [M28](MILESTONES.md#m28) |
| Interpret approximation operationally | §§3.1.1, 3.3.2–3.3.3 | [Complete-protocol error](../science/learning.md#cost-and-finite-precision) and channel discrimination | [M10](MILESTONES.md#m10), [M25](MILESTONES.md#m25), [M29](MILESTONES.md#m29) |
| Understand the meaning of equal capacity | §§8.2.1–8.2.2 | [Dephasing capacity specialization](../science/channels.md#5-exact-quantum-capacity) | [M12](MILESTONES.md#m12), [M17](MILESTONES.md#m17) |

For the last row, the definitions and theorem statement provide the needed orientation. The project's capacity proof then supplies the special degradability and symmetry argument. A first reading does not require reproducing the book's general coding-theorem proof.

## Notation dictionary

The main convention differences occur in [Watrous §2.2.2](https://jhwatrous.github.io/TQI.pdf), with entropy and channel distance defined in Chapters 5 and 3.

| Book notation | Repository notation or meaning |
|---|---|
| $`e_a`$, $`e_ae_b^*`$ | $`\lvert a\rangle`$, $`\lvert a\rangle\langle b\rvert`$ |
| $`A^*`$ | $`A^\dagger`$, the complex adjoint |
| $`\mathrm L(\mathcal X)`$, $`\mathrm D(\mathcal X)`$ | Operators and density operators on the register space |
| $`1_{\mathcal X}`$, $`1_{\mathrm L(\mathcal X)}`$ | Identity operator $`I`$ and identity channel $`\mathrm{id}`$, respectively |
| $`J(\Phi)`$ | Unnormalized Choi operator; here $`J_\nu=J(\mathcal D_\nu)/d`$ for input dimension $`d=q^n`$ |
| $`K(\Phi)`$ | The matrix representing the channel as a linear map on operators; called the superoperator here |
| $`H(\rho)`$ | $`S(\rho)`$; the repository reserves $`H(\nu)`$ for a classical distribution |
| Completely bounded trace norm | Diamond norm $`\lVert\Phi\rVert_\diamond`$; operational distances here include the factor $`1/2`$ |

The Choi normalization affects every stated eigenvalue: $`\mathrm{Tr}J(\mathcal D_\nu)=d`$, whereas $`\mathrm{Tr}J_\nu=1`$. The normalized Choi eigenvalues can therefore be read as probabilities. They are not the eigenvalues of $`K(\mathcal D_\nu)`$.

Two kinds of linear algebra coexist. Quantum amplitudes and density matrices are over $`\mathbb C`$. Secret vectors, phase labels, and regression coefficients are over $`\mathbb F_q`$. A transpose such as $`T^{\mathsf T}`$ in the LWE coordinate change is a finite-field matrix transpose; it should not be silently replaced by a complex adjoint. All entropies and capacities use base-two logarithms.

## What the project supplies

The following steps are supplied locally, with their research sources identified in [Related work](../references/RELATED_WORK.md). They are not asserted to be results from Watrous.

**Finite-field phase arithmetic.** For prime $`q`$, the symbols $`0,\ldots,q-1`$ label a $`q`$-dimensional quantum register. Arithmetic inside $`a\cdot s`$ and $`z\cdot a`$ is modulo $`q`$. The complex number $`\omega=e^{2\pi i/q}`$ converts that arithmetic into a physical phase. The project constructs its tensor-product shift and phase operators on $`n`$ such registers; this is the finite-field form used alongside the book's Weyl-channel language. See [M06](MILESTONES.md#m06) and [M13](MILESTONES.md#m13).

**A precise quantum source.** Each call supplies one mixed state formed from

```math
|\psi_{s,e}\rangle
=q^{-n/2}\sum_{a\in\mathbb F_q^n}|a\rangle|a\cdot s+e\rangle,
\qquad
\rho_s^\nu
=\mathbb E_{e\sim\chi,\,z\sim\nu}
 Z_z|\psi_{s,e}\rangle\langle\psi_{s,e}|Z_z^\dagger.
```

One sampled $`e`$ is shared across all branches within a call. Fresh $`e,z`$ are used on the next call, while $`s`$ remains fixed. The learner receives neither randomness nor an inverse preparation circuit. A source that knows $`s`$ can prepare these states; a collection of classical LWE samples does not automatically provide them. This distinction is the [access contract](../science/model.md#access-contract), developed in [M07](MILESTONES.md#m07).

**The computational question.** The task is to recover $`s`$ from repeated emissions. Classical-input LWE instead provides measured pairs $`(a,a\cdot s+e)`$. The [hardness proof](../science/hardness.md) simulates the linear-noise source from a smaller classical LWE instance, including arbitrary subsequent quantum processing by the learner. Its hard/easy conclusion invokes a stated asymptotic LWE assumption. Quantum-channel definitions alone do not supply that assumption.

**The algebraic learner and resource account.** The [learning proof](../science/learning.md) derives a finite-field regression from the cubic phase law and bounds the number of raw copies. [Implementation](../science/implementation.md) supplies preparation, readout, precision, and dephasing costs. These steps turn a state-level identity into an algorithm with a specified interface. They occupy [M18–M27](MILESTONES.md#m18), after the channel foundations.

## Reading the physical meaning

### One process, three useful descriptions

For a classical phase law $`\nu`$, the project uses

```math
\mathcal D_\nu(X)=\sum_z\nu(z)Z_zXZ_z^\dagger,
\qquad Z_z|a\rangle=\omega^{z\cdot a}|a\rangle.
```

In the **random-unitary description**, a run applies a product of local phase gates. Correlation resides in the joint choice of their labels, even though each gate acts locally. The Kraus operators are $`\sqrt{\nu(z)}Z_z`$.

In the **entrywise description**, the same channel obeys

```math
\mathcal D_\nu(|a\rangle\langle a'|)
=\widehat\nu(a-a')|a\rangle\langle a'|,
\qquad
\widehat\nu(\delta)=\sum_z\nu(z)\omega^{z\cdot\delta}.
```

Every diagonal entry is unchanged. An off-diagonal entry survives according to a Fourier coefficient of the phase distribution. This is the project's explicit Schur multiplier. Equality of local phase marginals constrains only some of these coefficients; it does not identify the complete channel.

In the **environment description**, the isometry is

```math
|a\rangle\longmapsto|a\rangle|E_a\rangle,
\qquad
|E_a\rangle=\sum_z\sqrt{\nu(z)}\omega^{z\cdot a}|z\rangle_E.
```

Discarding the environment multiplies a coherence by $`\langle E_{a'}|E_a\rangle=\widehat\nu(a-a')`$. Thus the overlap of environmental records determines what the system retains. [Channel invariants](../science/channels.md) makes these three descriptions agree exactly; [Implementation](../science/implementation.md) realizes the source with explicitly counted registers and gates.

### Equal numbers can answer different operational questions

For these phase channels the project obtains

```math
C_{\mathrm{rel}}(\rho_s^\nu)=n\log_2q-H(\nu),
\qquad
Q(\mathcal D_\nu)=n\log_2q-H(\nu).
```

The first expression compares a prescribed state with its dephased version in the specified basis. The second is an asymptotic communication rate with optimized encoders and decoders, measured in qubits per use of the entire $`n`$-input channel. Neither quantity specifies the computation required to extract an unknown $`s`$ from this source. The shared formula is established by separate arguments in [the channel proof](../science/channels.md), using the primary coherence and capacity results cited there.

The relevant distinction is also visible within the book's channel representations: the two normalized Choi spectra agree, while the superoperator singular values differ. A spectrum of a state and a spectrum of a map summarize different objects.

## Worked example: two inputs over five symbols

This is a finite illustration of the existing theorem, using $`n=2`$ and $`q=5`$. It demonstrates the algebra and conventions; a one-dimensional residual problem at this size is not a cryptographic hardness instance. It connects [M15–M17](MILESTONES.md#m15) to [M20–M21](MILESTONES.md#m20).

### The same local noise and the same spectra

Draw $`x`$ uniformly from $`\mathbb F_5`$. The two possible phase laws are

```math
z_L=(x,x),\qquad z_C=(x,x^3).
```

| $`x`$ | Linear phase label | Cubic phase label |
|---:|---:|---:|
| 0 | $`(0,0)`$ | $`(0,0)`$ |
| 1 | $`(1,1)`$ | $`(1,1)`$ |
| 2 | $`(2,2)`$ | $`(2,3)`$ |
| 3 | $`(3,3)`$ | $`(3,2)`$ |
| 4 | $`(4,4)`$ | $`(4,4)`$ |

Each individual coordinate is uniform in either column. Accordingly, the reduced channel on either one input is complete computational dephasing. The joint laws differ in two of their five support points.

The input dimension is $`d=25`$. Each normalized Choi state has five nonzero eigenvalues $`1/5`$; the unnormalized book convention gives five eigenvalues $`5`$. For any common additive-error law $`\chi`$, the complete source eigenvalues are $`\chi(e)/5`$, repeated five times for each error label, together with zeros. The source acts on a $`25\times5=125`$ dimensional space. Consequently,

```math
S(\rho_s^\nu)=\log_2 5+H(\chi),\qquad
S(\rho_s^{\mathrm{cl}})=2\log_2 5+H(\chi),
\qquad C_{\mathrm{rel}}=Q=\log_2 5.
```

These values do not yet say how the secret is recovered.

### A complete cubic recovery transcript

The positive Fourier convention of the project gives the measured outcome

```math
(u_1,u_2,k),\qquad u=-ks-z.
```

For a nonzero $`k`$, cubic support implies

```math
b:=\frac{u_2-u_1^3}{k}
=3s_1u_1^2+3ks_1^2u_1+k^2s_1^3-s_2
\pmod5.
```

Treat $`\theta=(\alpha,\beta,\gamma,\zeta)=(s_1,s_1^2,s_1^3,s_2)`$ as four linear unknowns. The following is one possible transcript of four accepted outcomes; the rows are not chosen queries to the source.

| $`(u_1,u_2,k)`$ | Feature row $`(3u_1^2,3ku_1,k^2,-1)`$ | Response $`b`$ |
|---|---|---:|
| $`(0,3,1)`$ | $`(0,0,1,4)`$ | 3 |
| $`(0,2,2)`$ | $`(0,0,4,4)`$ | 1 |
| $`(1,0,1)`$ | $`(3,3,1,4)`$ | 4 |
| $`(1,1,2)`$ | $`(3,1,4,4)`$ | 0 |

All operations are modulo five, including division: $`2^{-1}=3`$. The first two rows give

```math
\gamma-\zeta=3,\qquad4\gamma-\zeta=1.
```

Subtracting yields $`3\gamma=3`$, so $`\gamma=1`$ and $`\zeta=3`$. Substituting these into the last two rows gives

```math
3\alpha+3\beta=1,\qquad3\alpha+\beta=4.
```

Hence $`2\beta=2`$, $`\beta=1`$, and $`\alpha=1`$. The recovered secret is

```math
s=(1,3),\qquad s_1^2=1,\qquad s_1^3=1.
```

The lifted coordinates satisfy their promised consistency relations. The corresponding hidden values of $`x=-u_1-ks_1`$ are $`4,3,3,2`$, which reproduce all four displayed outcomes using $`z_C=(x,x^3)`$. No value of $`e`$ was needed: it affects a phase before this measurement, not its probabilities.

This particular transcript has full rank. Other four-outcome transcripts need not. The [fixed raw-copy theorem](../science/learning.md#theorem-a-fixed-raw-copy-budget) accounts for random rows, repeated rows, and discarded $`k=0`$ outcomes. It is the guarantee used by the algorithm; the example does not replace it.

### What the linear source reveals instead

For the same secret and $`z_L=(x,x)`$, every nonzero-$`k`$ Fourier outcome obeys

```math
u_2-u_1=-k(s_2-s_1),\qquad
\kappa:=s_2-s_1=2.
```

This readout repeatedly supplies the same quotient coordinate. To see the remaining task, use input coordinates $`X=a_1+a_2`$ and $`Y=a_2`$. The source's output label is

```math
a_1s_1+a_2s_2+e=Xs_1+Y\kappa+e.
```

After learning $`\kappa`$, subtract $`Y\kappa`$ from a fresh copy. What remains is exactly a classical pair $`(X,Xs_1+e)`$ and a known coherent register. The [two-way source reduction](../science/hardness.md) proves this for arbitrary collective learners and for general dimension. It supplies the asymptotic computational interpretation that this small arithmetic example cannot.

### How an extra local dephasing changes the example

Both graph laws retain only coherences involving both inputs. Adding dephasing mixtures with probabilities $`p_1,p_2`$ gives

```math
\widetilde\rho_s^\nu
=\eta\rho_s^\nu+(1-\eta)\rho_s^{\mathrm{cl}},
\qquad\eta=(1-p_1)(1-p_2).
```

Fully dephasing either input makes $`\eta=0`$ and leaves the classical source. This is the two-register instance of [the exact fragility identity](../science/implementation.md#5-exact-effect-of-independent-local-dephasing), not a statement about arbitrary hardware noise. The general identity and its asymptotic implications are developed in [M26–M27](MILESTONES.md#m26).

## Returning to the general theorem

The example separates three tasks: describe a physical channel, calculate its state and communication diagnostics, and infer a secret from its prescribed outputs. Watrous supplies the underlying operator and information language. The project's finite-field source transformations and recovery algorithm connect that language to the third task.

Continue with [M14](MILESTONES.md#m14) to assemble the foundations, [M19–M22](MILESTONES.md#m19) for the two computational directions and sample accounting, and [M30](MILESTONES.md#m30) for the theorem with all assumptions and scope qualifications. The [verification suite](../verification/README.md) checks finite identities and recovery instances; the general proofs and the stated LWE assumption have distinct roles.
