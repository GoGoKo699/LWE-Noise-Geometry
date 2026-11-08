# A cutting statistic that does not separate the phase channels

[Science guide](README.md) · [Channel invariants](channels.md) · [Source interpretation](interpretation.md)

The linear and cubic channels are distinct, and their prescribed coherent LWE sources have different recovery complexity under the stated hardness assumption. Those facts do not imply a strict ordering for every operational task. At $`n=2,q=5`$, using the channels as joint noise on two laboratories' persistent memories gives the same exact two-wire cutting extent:

```math
\boxed{\Gamma_L=\Gamma_C=49.}
```

The complete proof and construction belong to [Quantum Memory Circuit Cutting, correlated phase memory](https://github.com/GoGoKo699/Quantum-Memory-Circuit-Cutting/blob/306d063ce1583e0df77444217e7db06461ba1915/science/correlated-phase-memory.md). That account supplies the strict causal cutting model, the spatial separability converse, the direct upper bound $`97-16\sqrt5`$, and the complete parity instrument improving it to 49. This page states the model and the mechanism needed to understand the consequence independently. The phase laws and their learning interpretation remain authoritative here in [model.md](model.md) and [channels.md](channels.md).

## 1. The same channels in a different task

For $`x`$ uniform in $`\mathbb F_5`$, the two phase labels are $`(x,x)`$ and $`(x,x^3)`$. In the source theorem these act on the two noisy input registers of a supplied secret-dependent state. In the cutting comparison they instead act, once, on the two laboratories' private memories:

```math
\mathcal N_f(\rho)=\frac15\sum_{x\in\mathbb F_5}
 (Z^x\otimes Z^{f(x)})\rho(Z^x\otimes Z^{f(x)})^\dagger,
\qquad Z|j\rangle=\omega^j|j\rangle,
\qquad \omega=e^{2\pi i/5},
```

where $`f(x)=x`$ or $`f(x)=x^3`$. This is the full correlated channel, not the product of its completely dephasing marginals. Conditional on every permitted pre-gap classical history, the hidden draw is fresh and uniform; its flag and environment are inaccessible.

The target is two ordered five-dimensional identity wires from Alice to Bob. Alice receives the first unknown input, and Bob releases its output before the gap. Only after the gap does the second unknown input arrive. The cutter may not borrow released outputs or external references as storage. At most one five-level private quantum register per laboratory crosses the gap. There is no initial shared entanglement or quantum communication; local instruments, transient workspace and classical communication within the slots are allowed.

The cost concerns exact signed simulation of this open process, including arbitrary external reference systems and causal interventions. An allowed atom has the form

```math
\mathcal F=\sum_h s_h\mathcal C_h,
\qquad |s_h|\le1,
```

where $`\{\mathcal C_h\}`$ is a complete physical causal instrument obeying those resources. Every outcome retains its physical probability, including outcomes assigned negative scores. A normalized successful filter branch is not free. The extent is the infimum of $`\sum_k|a_k|`$ in $`\mathcal I^{(2)}=\sum_k a_k\mathcal F_k`$, with finite-round protocols and their operational closure included.

This task supplies controlled resource preparation and accepts arbitrary incoming states. It supplies neither copies of $`\rho_s^\nu`$ nor access to its secret-dependent encoder. There is no reduction here identifying cutting extent with source-learning complexity or with communication capacity.

## 2. A universal lower bound

A normalized Bell-probe tester gives target Choi state $`\Phi_{25}=\Phi_5\otimes\Phi_5`$ across the spatial partition of Alice's two input references and Bob's two outputs. Every positive physical outcome Choi operator $`X`$ is spatially separable: local operations, classical communication and a mixture of product phase unitaries preserve that property. Hence

```math
0\le\operatorname{Tr}(\Phi_{25}X)\le\frac{\operatorname{Tr}X}{25},
\qquad
W=50\Phi_{25}-I_{625},
\qquad
|\operatorname{Tr}(WX)|\le\operatorname{Tr}X.
```

Completeness gives $`\sum_h\operatorname{Tr}J(\mathcal C_h)=1`$. Bounded scores therefore give $`|\operatorname{Tr}WJ(\mathcal F)|\le1`$. Since the target evaluates to 49, both extents are at least 49. The argument includes arbitrary filtering and adaptive records. Expanding the hidden phase sum mathematically does not make the flag available to the protocol. The continuous witness also bounds operational limits of finite-round protocols.

The witness is the inherited spatial robustness argument; it is not a new LWE converse. The new issue is whether the actual correlated noisy memory can attain its bound with a complete instrument.

## 3. Why a complete parity instrument attains the bound

For $`j=1,2`$, use the symmetric and antisymmetric memory vectors

```math
|s_j\rangle=\frac{|j\rangle+|-j\rangle}{\sqrt2},
\qquad
|a_j\rangle=\frac{|j\rangle-|-j\rangle}{\sqrt2}.
```

Each laboratory prepares its first resource port and its memory in

```math
|\psi\rangle=\frac{|1\rangle|s_1\rangle+|2\rangle|s_2\rangle}{\sqrt2}.
```

After the gap it emits its second resource port using the two-outcome decoder

```math
K_e=|0\rangle\langle0|+|1\rangle\langle s_1|+|2\rangle\langle s_2|,
\qquad
K_o=|2\rangle\langle a_1|+|1\rangle\langle a_2|.
```

The five memory vectors $`0,s_1,s_2,a_1,a_2`$ are orthonormal, so $`K_e^\dagger K_e+K_o^\dagger K_o=I_5`$. Score +1 when the two accessible parity outcomes agree and −1 when they differ. All four outcome pairs remain in the physical instrument.

With $`\theta_x=2\pi x/5`$, the unnormalized local two-time vectors are

```math
|e_x\rangle=\frac{\cos\theta_x|11\rangle+\cos2\theta_x|22\rangle}{\sqrt2},
\qquad
|o_x\rangle=\frac{i(\sin\theta_x|12\rangle+\sin2\theta_x|21\rangle)}{\sqrt2}.
```

Over $`\mathbb F_5`$, $`x^3=\epsilon_x x`$ with $`\epsilon_x\in\{+1,-1\}`$. Consequently $`e_{x^3}=e_x`$ and $`o_{x^3}=\epsilon_xo_x`$. The density operators of the local parity branches are therefore the same for the paired linear and cubic errors, although the channels themselves are not equal. For $`E_x=|e_x\rangle\langle e_x|`$ and $`O_x=|o_x\rangle\langle o_x|`$, the signed resource is

```math
F_{\mathrm{raw}}=\frac15\sum_x(E_x-O_x)_A\otimes(E_x-O_x)_B.
```

The local labels in this expression denote two-time resource ports; Bell tests regroup them by spatial slot pairs. Apply an independent bilateral isotropic twirl $`U\otimes\overline U`$ to each pair. Finite exact twirls suffice. Define

```math
\Phi=\Phi_5,\qquad R=\frac{I_{25}-\Phi}{24},\qquad
\rho_+=\frac15\Phi+\frac45R,\qquad \rho_-=R,\qquad
V_{ab}=\rho_a\otimes\rho_b.
```

Both $`\rho_+`$ and $`\rho_-`$ are separable preparations, obtained by twirling aligned or orthogonal basis products. The four relevant moments of the scored resource are

| Moment | Value |
|---|---:|
| $`\operatorname{Tr}F_{\mathrm{raw}}`$ | $`1/4`$ |
| First marginal Bell overlap | $`1/20`$ |
| Second marginal Bell overlap | $`1/40`$ |
| Joint Bell overlap | $`1/40`$ |

These values determine the complete twirled operator:

```math
F=\frac1{40}\Phi\otimes\Phi+\frac1{40}\Phi\otimes R+\frac15R\otimes R.
```

In particular, $`F`$ has signed trace $`1/4`$. It is a bounded-score complete-instrument atom and must not be normalized into a free successful branch. Its marginal asymmetry also matters: replacing the unequal coefficients below by equal ones would not give the displayed identity.

Direct substitution in the four sectors $`\Phi\Phi,\Phi R,R\Phi,RR`$ gives

```math
\boxed{\Phi_5\otimes\Phi_5
=5V_{++}+32F-8V_{+-}-4V_{-+}.}
```

The coefficient extent is $`5+32+8+4=49`$. This proves the attainable bound for both noise channels, matching the universal lower bound.

## 4. Timing and information access

The resource calculation has a strict streaming implementation. The first resource port is consumed in teleporting the first actual input, and Bob corrects and releases the first output before the gap. Only the one memory at each laboratory persists. The decoder emits the second resource port after the noise, and the second actual input is then teleported. The final score may be applied retrospectively using the accessible parity labels.

First-port rotations and teleportation maps act on tensor factors disjoint from the memory noise and later decoder. Commuting those maps proves equality with the simultaneous resource calculation without moving a future input earlier or retaining a released output. Slotwise twirling makes the resource Bell diagonal; slotwise teleportation then converts its full operator identity into equality of the open process against arbitrary causal testers. Neither operation measures or conditions the score on the hidden phase draw.

The earlier cubic upper bound $`97-16\sqrt5\approx61.2229`$ is valid but nonoptimal. The [complete proof](https://github.com/GoGoKo699/Quantum-Memory-Circuit-Cutting/blob/306d063ce1583e0df77444217e7db06461ba1915/science/correlated-phase-memory.md) certifies it directly with deterministic rank-two temporal cats and then gives the parity construction above. Restricting attention to deterministic normalized resources or invertible filters would miss the complete scored instrument attaining 49.

## 5. What transfers between the projects

LWE Noise Geometry supplies the explicit phase laws and their matched diagnostics, channel distinctions and source-learning comparison. Quantum Memory Circuit Cutting supplies the causal cutting model, instrument accounting, spatial witness and streaming resource-to-process method. The shared new consequence is the exact parity construction proving equal extent for this finite comparison. The full proof has one authoritative home in the cutting repository.

The conclusion is specific to $`q=5`$, two ordered identity wires, one five-level memory per laboratory, and the stated inaccessible-flag model. It does not establish a general-prime or many-slot law, equal optimal costs for all tasks, channel-unitary equivalence, or equal complexity for learning from the prescribed source. The [different superoperator singular values](channels.md#62-choi-isospectrality-is-not-channel-unitary-equivalence) and the [source reductions](hardness.md) retain their stated meaning.

Watrous (2018), §§2.2–2.3, §6.1 and §6.3.1, supplies the common channel, instrument, separability and teleportation language. The phase graph and parity identity are project-specific results. The [finite circuit-cutting check](../verification/circuit_cutting_checks.py) verifies the actual noisy branch contractions, complete decoder and full twirled identity; the lower bound and arbitrary-tester equality remain analytical arguments.
