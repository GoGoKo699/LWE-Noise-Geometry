# Thirty milestones through the noise-geometry comparison

[Learning guide](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific account](../science/README.md)

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). Section references below point to the [author-hosted manuscript][watrous]; the [author's book page][watrous-page] identifies the published book. The manuscript is linked, not redistributed.

The map has two phases. **M01–M14** establish the representations, access assumptions, information quantities, and algebra used by this project. **M15–M30** follow the comparison from its two local phase laws through recovery, implementation, fragility, and interpretation. Fourteen preliminary milestones are appropriate here because the argument combines a channel theorem, a computational reduction, and a statistical recovery algorithm. Both phases end in synthesis.

Watrous supplies the quantum-information framework. Classical-input LWE, finite-field polynomial recovery, the shared-error source, and their particular reductions are supplied by the repository's canonical science pages and the primary research cited there. The milestone text identifies conceptual destinations and dependencies; it does not replace those proofs. The [bridge's worked example](WATROUS_BRIDGE.md#worked-example-two-inputs-over-five-symbols) provides one finite illustration across several milestones.

## Phase I — Background and preliminaries

<a id="m01"></a>

### M01 — Registers and two kinds of linear algebra

**Central question.** How can a quantum register have finite-field labels while its state space remains a complex vector space?

**Understanding target.** The source uses $`n`$ input registers and one output register, each with $`q`$ computational labels. Label arithmetic, dot products, and later Gaussian elimination occur in $`\mathbb F_q`$. State amplitudes, inner products, tensor products, and operator spectra occur over $`\mathbb C`$. The dimension $`q^n`$ of the input state space is different from the $`n`$ field coordinates describing the secret. A binary implementation uses $`\lceil\log_2q\rceil`$ qubits per field register, with a specified valid subspace.

**Dependencies and story role.** This is the starting point. It fixes the meaning of dimension before rank appears in three different roles: a linear record, a density operator, and a regression matrix.

**Conceptual connection.** A modular coordinate change can be a permutation unitary on basis states. Its finite-field invertibility and the corresponding complex operator's unitarity describe compatible aspects of one operation.

**Sources.** [Watrous §§1.1.1–1.1.2 and 2.1.1][watrous]; [registers and arithmetic](../science/model.md#registers-arithmetic-and-distributions); [binary field encoding](../science/implementation.md#1-source-preparation-without-a-data-loading-oracle). The finite-field conventions are local to the project.

<a id="m02"></a>

### M02 — Pure states, mixtures, and independent emissions

**Central question.** Which randomness is coherent inside a sample, and which randomness is averaged between samples?

**Understanding target.** A fixed pair of classical labels $`(e,z)`$ specifies a pure source branch. Averaging those labels produces a density operator. The input label $`a`$ remains coherent within the branch, while one additive error $`e`$ is shared across all its amplitudes. A new independent pair of random labels is used for every emission, with the same secret retained. A mixture over a scalar error is therefore different from a state with independently chosen errors indexed by every $`a`$.

**Dependencies and story role.** M01 supplies the registers. This milestone identifies the actual random experiment before channels, spectra, or computational claims are attached to it. Independence between copies will later justify the regression probability bound and the trace-distance hybrid.

**Conceptual connection.** Classical uncertainty about which pure state was prepared does not grant the receiver the preparation label or a purification. The same density operator can have several ensemble descriptions with different inaccessible records.

**Sources.** [Watrous §§1.2.2 and 2.1.2][watrous]; [an emitted quantum sample](../science/model.md#an-emitted-quantum-sample); [source-model comparison](../references/RELATED_WORK.md#1-the-access-model-matters).

<a id="m03"></a>

### M03 — Reductions and hidden environments

**Central question.** What does an observer retain when part of a quantum system is discarded?

**Understanding target.** Partial trace describes discarded input registers and hidden environments. Equality of reduced states is weaker than equality of the global states. Equality of reduced channels for arbitrary inputs and arbitrary reference systems is stronger than matching the marginals of one probe. In this project, the relevant proper subsets are subsets of the $`n`$ noisy input registers; retaining all inputs while discarding only the scalar output is a different operation.

**Dependencies and story role.** M02 distinguishes mixtures from pure branches. The present milestone supplies the subsystem language needed for the all-proper-marginal claim in M15 and for interpreting a bath that is never revealed to the learner.

**Conceptual connection.** A hidden environment can preserve a record of an input property even when no local observer can see the global correlation. The source model specifies which systems exist mathematically and which are actually accessible.

**Sources.** [Watrous §2.1.3 and §2.2.1][watrous]; [reduced-channel identity](../science/channels.md#proposition-2-reduced-channel-identity-including-references); [subsystem qualification](../science/model.md#what-is-matched-and-what-is-not-implied).

<a id="m04"></a>

### M04 — Channels and their representations

**Central question.** How do a random phase operation, a Kraus sum, and a system–environment interaction describe one channel?

**Understanding target.** The phase law $`\nu`$ defines a completely positive, trace-preserving map by averaging the unitary conjugations $`Z_z(\cdot)Z_z^\dagger`$. A Kraus representation, a Choi operator, and an isometric dilation encode the same map in different ways. None of these descriptions automatically gives the receiver control of the environment. The phase channel itself is secret-independent; the secret-dependent source additionally includes the encoder $`U_s`$ and the error register.

**Dependencies and story role.** M02–M03 supply mixed states and inaccessible systems. This milestone separates the channel from the source on which it acts, preventing a statement about communication through a known map from becoming an unsupported statement about learning a secret.

**Conceptual connection.** The complementary channel records what reaches the environment. It will explain both the physical bath accounting and the degradability argument for capacity, without changing the learner's access contract.

**Sources.** [Watrous §§2.2.1–2.2.2][watrous]; [channel definitions](../science/channels.md#1-definitions-and-conventions); [environmental representation](../science/channels.md#environmental-dimension-and-entropy); [source factorization](../science/model.md#a-useful-factorization).

<a id="m05"></a>

### M05 — Measurements and classical data

**Central question.** Why do computational-basis and Fourier measurements of the same source define different learning data?

**Understanding target.** A measurement produces a classical probability distribution through its effects on the density operator. Computational-basis measurement gives an ordinary LWE pair for every phase law in the construction. A Fourier measurement can instead expose a relation involving the phase label and the secret. Product measurements act separately on registers, but their complete joint outcome can still carry a correlation involving every register.

**Dependencies and story role.** M02 and M04 define the state and channel. This milestone establishes the two data interfaces that are compared later: the common classical diagonal and the phase-sensitive readout. It also separates a product measurement from a restriction to small subsets of its outcomes.

**Conceptual connection.** Measurement is an information-processing map. Discarding phase information before processing can change the available inference task even though a later quantum computer may process the resulting classical samples without restriction.

**Sources.** [Watrous §§2.3.1–2.3.2][watrous]; [computational measurement and access](../science/model.md#access-contract); [Fourier readout](../science/learning.md#fourier-readout); [global processing of local measurements](../science/interpretation.md#local-invisibility-does-not-prevent-global-channel-discrimination).

<a id="m06"></a>

### M06 — Fourier phases and dephasing

**Central question.** How does averaging phase gates determine exactly which matrix elements survive?

**Understanding target.** The positive Fourier convention and $`Z_z|a\rangle=\omega^{z\cdot a}|a\rangle`$ fix the signs used throughout the project. The phase channel multiplies $`|a\rangle\langle b|`$ by the characteristic function $`\widehat\nu(a-b)`$. Uniform phase averaging removes off-diagonal entries, while structured averaging can preserve selected differences. Thus the same channel has a random-unitary description and a diagonal action on an operator basis.

**Dependencies and story role.** M01 supplies label arithmetic, M04 channel representations, and M05 measurement. This milestone connects those descriptions and provides the common mechanism behind linear fibers, cubic readout, and the later local-dephasing identity.

**Conceptual connection.** The probability distribution $`\nu`$ and its Fourier multipliers contain the same global information but organize it differently. Choi eigenvalues will follow $`\nu`$; the superoperator action will follow $`\widehat\nu`$. Confusing these two spectra would erase a central distinction.

**Sources.** [Watrous §§4.1.1–4.1.3][watrous]; [phase-channel conventions](../science/channels.md#1-definitions-and-conventions); [Fourier multipliers](../science/channels.md#unitarity); [readout signs](../science/learning.md#fourier-readout). The explicit finite-field Fourier calculation is supplied locally.

<a id="m07"></a>

### M07 — Classical-input LWE and the access contract

**Central question.** What computational problem supplies the hard branch, and what additional resource does the quantum source provide?

**Understanding target.** Classical-input search LWE gives independent pairs $`(x,x\cdot u+e)`$ for a fixed uniform secret. The adversary may use quantum computation, but its input is classical. The project's source instead emits coherent states prepared by a holder who knows the secret. State copies do not include a sampler's inverse, its random seed, chosen inputs, or repeated evaluations under a common error. The hardness statement is an explicit asymptotic assumption for a selected modulus and error family.

**Dependencies and story role.** M01 and M05 distinguish register labels and measurement outputs. This milestone identifies the baseline that the exact reduction in M19 must simulate, rather than treating every form of “quantum LWE” as interchangeable.

**Conceptual connection.** An identical computational diagonal establishes a common measurement distribution, not a general construction of coherent copies from classical samples. Simulation requires its own algorithm and access argument.

**Sources.** [Watrous §2.3.1][watrous] supplies the measurement framework; [classical problem and assumption](../science/hardness.md#the-classical-problem-and-its-assumption), [access contract](../science/model.md#access-contract), and [Regev's primary paper](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) supply the LWE content.

<a id="m08"></a>

### M08 — Spectra, entropy, and coherence

**Central question.** Which features of a state depend only on its eigenvalues, and which also depend on a chosen basis?

**Understanding target.** Rank, purity, and spectral entropies are functions of the spectrum. The source factorization makes its eigenvalues products $`\nu(z)\chi(e)`$, independent of the secret. Computational dephasing changes the state while retaining its classical diagonal. Relative-entropy coherence compares the entropy before and after that specific dephasing; its basis is fixed by the classical LWE interface, not optimized independently for each channel.

**Dependencies and story role.** M02 supplies density operators and M06 the orthogonal Fourier labels. This milestone establishes the quantities that can match automatically when phase laws have the same probability multiset, before their computational consequences are considered.

**Conceptual connection.** Unitary conjugation preserves eigenvalues but can rearrange which basis-dependent constraints reveal an unknown parameter. Equal entropy therefore does not identify an inference algorithm or establish equivalent state access.

**Sources.** [Watrous §1.1.3 and §§5.1.1, 5.2.1–5.2.2][watrous]; [source spectra and coherence](../science/channels.md#3-source-spectra-entropy-and-coherence); [coherence attribution](../references/RELATED_WORK.md#6-coherence-channel-diagnostics-and-capacity). The coherence measure and its source-specific formula are supplied in the local account.

<a id="m09"></a>

### M09 — Choi states and channel diagnostics

**Central question.** What does matching a channel's Choi spectrum establish, and what does it leave unspecified?

**Understanding target.** The normalized Choi state results from applying the channel to one half of a normalized maximally entangled state. For phase channels, orthogonal phase-labelled components make its nonzero eigenvalues equal to the phase probabilities. Choi rank gives the minimal environment dimension. This representation differs from the matrix representing the channel on operator space. Their spectra need not agree, and equal Choi spectra need not imply equivalent channel actions.

**Dependencies and story role.** M04 provides channel representations and M08 spectral quantities. The present milestone organizes the diagnostics later collected in M16 and the distinctions later proved in M17 and M29.

**Conceptual connection.** A scalar summary can coincide because both distributions have the same support size, without the corresponding maps agreeing on every input. Fidelity and unitarity are useful diagnostics whose operational definitions must accompany their numerical equality.

**Sources.** [Watrous §2.2.2 and §4.2.2][watrous]; [normalized Choi spectrum and metrics](../science/channels.md#4-choi-spectra-and-scalar-channel-metrics); [excluded channel-unitary equivalence](../science/channels.md#62-choi-isospectrality-is-not-channel-unitary-equivalence). The repository uses a normalized Choi state; Watrous's channel representation must be translated with that normalization.

<a id="m10"></a>

### M10 — Operational distances and accumulated error

**Central question.** How does closeness of states or channels control the success probability of an entire learning procedure?

**Understanding target.** Trace distance bounds the change in any event probability after processing a state. The diamond norm accounts for channel inputs entangled with references. The repository uses one half of these norms as operational distances. A telescoping hybrid accumulates per-copy errors across a fixed number of independent emissions. A small marginal error for each register or each copy does not alone justify a bound for arbitrary correlated noise.

**Dependencies and story role.** M03–M05 provide references, channels, and measurements. This milestone supplies the common language for compilation accuracy, noisy-source simulation, and global channel discrimination, which are distinct applications of one operational principle.

**Conceptual connection.** A distance bound becomes a computational reduction only when an efficient simulator produces the comparison state. Conversely, a distinguishability bound does not by itself identify a secret-recovery algorithm.

**Sources.** [Watrous §3.1.1 and §§3.3.1–3.3.3][watrous]; [fixed-protocol error budget](../science/implementation.md#a-fixed-protocol-has-an-explicit-error-budget); [conditional noisy-source simulation](../science/implementation.md#corollary-52-a-conditional-hardness-regime). Watrous's completely bounded trace norm is the diamond norm used here.

<a id="m11"></a>

### M11 — Ensemble information and identifiability

**Central question.** Why can equal secret-conditioned spectra coexist with different information about a random secret?

**Understanding target.** An ensemble includes both a prior on the secret and one state for each secret value. Its average state can change even when every individual state's spectrum is unchanged. Holevo information, mutual information in a specified measurement, many-copy identifiability, and computational recovery are different quantities. Repeated samples may supply new constraints or repeatedly expose the same quotient; the number of bits in one sample does not distinguish those possibilities.

**Dependencies and story role.** M05 supplies classical outcomes and M08 entropy. This milestone prevents the later computational comparison from silently becoming an assertion of equal Holevo information or an information-theoretic lower bound for narrow-error LWE.

**Conceptual connection.** Identifiability asks whether different secrets induce distinguishable data in principle. Efficient learning additionally asks whether those distinctions can be converted into the secret with bounded resources.

**Sources.** [Watrous §§5.1.1, 5.2.1, and 5.3.3][watrous]; [Fourier mutual information](../science/interpretation.md#the-fourier-measurement-has-equal-single-copy-mutual-information); [Holevo distinction](../science/interpretation.md#equal-conditional-spectra-do-not-imply-equal-holevo-information); [narrow-error identifiability](../science/interpretation.md#narrow-errors-can-make-the-hard-branch-identifiable).

<a id="m12"></a>

### M12 — Coherent information and quantum capacity

**Central question.** What operational task does quantum capacity quantify, and why is it different from the present inference task?

**Understanding target.** Quantum capacity concerns reliable quantum communication using optimized encodings and decodings across independent invocations of a channel. Coherent information compares the entropies of its output and complement. Degradability provides a special single-letter optimization, while covariance and concavity can identify an optimizing input. The capacity units here are qubits per invocation of the whole $`n`$-register channel, not per noisy site or per secret coordinate.

**Dependencies and story role.** M04 supplies complements, M08 entropy, and M10 operational accuracy. This milestone gives the interpretation of the capacity match before its specialized proof is used in M17.

**Conceptual connection.** Communication permits a chosen code. The learner instead receives a prescribed secret-dependent source. Equal optimal communication rates can therefore coexist with different recovery complexity for that source without contradicting a capacity theorem.

**Sources.** [Watrous §§8.2.1–8.2.2][watrous]; [phase-channel capacity proof](../science/channels.md#5-exact-quantum-capacity); [capacity attribution and scope](../references/RELATED_WORK.md#6-coherence-channel-diagnostics-and-capacity). The degradability specialization and exact phase-channel formula are supplied locally with their primary research citations.

<a id="m13"></a>

### M13 — Finite-field graphs and polynomial features

**Central question.** How can a nonlinear constraint become a linear recovery problem without becoming a linear noise law?

**Understanding target.** A permutation graph can have uniform projections onto all proper coordinate subsets while retaining an exact global equation. Polynomial expansion can express a translated graph equation as a linear relation in lifted coefficients of the unknown secret. The design matrix then lives over $`\mathbb F_q`$. A polynomial zero bound controls whether random feature rows distinguish every nonzero coefficient direction; it is separate from a numerical conditioning argument over the real numbers.

**Dependencies and story role.** M01 fixes the two fields of arithmetic, and M07 defines the unknown-secret task. This milestone supplies the algebraic tools needed by both the marginal construction and the learner, without assuming that the anchor contains a finite-field learning algorithm.

**Conceptual connection.** Nonlinearity supplies additional identifiable coefficients, while linear algebra solves for those coefficients after measurement. This division locates the quantum and classical parts of the algorithm.

**Sources.** [Watrous §§1.1.2 and 1.2.2][watrous] provide general linear-algebra and probability language; [permutation-graph marginals](../science/channels.md#proposition-1-uniform-proper-marginals), [polynomial relation](../science/learning.md#the-exact-polynomial-relation), and [zero-bound proof](../science/learning.md#proof-of-the-copy-bound) supply the finite-field material.

<a id="m14"></a>

### M14 — Background synthesis: a source-to-learning pipeline

**Central question.** How do state preparation, channel action, measurement, and inference fit into one well-defined comparison?

**Understanding target.** The complete pipeline has a secret and error law, a secret-dependent encoder, a public phase channel, independent emitted copies, a measurement, and classical post-processing. Each claim belongs to a particular level: source spectra, reduced channels, communication capacity, measurement information, or secret-recovery complexity. The common classical diagonal and matched diagnostics constrain the comparison without replacing the access contract or the LWE assumption.

**Dependencies and story role.** M01–M13 supply the complete preliminary vocabulary. This is the first synthesis: it fixes the interfaces and quantities whose relationships the narrative phase will establish, while distinguishing inherited quantum-information tools from the project's finite-field reductions.

**Conceptual connection.** A single experiment supports several valid mathematical descriptions. The separation depends on relating those descriptions through explicit maps rather than treating one diagnostic as a universal measure of learning power.

**Sources.** [Watrous §§2.1–2.3, 5.2.1, and 8.2.1][watrous]; [source model and main theorem](../science/model.md#main-theorem); [proof dependencies](../science/model.md#proof-dependencies); [bridge](WATROUS_BRIDGE.md#what-the-project-supplies). The next phase follows these canonical proof dependencies.

## Phase II — Narrative and innovation

<a id="m15"></a>

### M15 — The linear and cubic graph pair

**Central question.** How can two different global phase laws agree on every proper input subsystem?

**Understanding target.** The phase labels are uniform on either $`L=\{(x,\sum_i x_i)\}`$ or $`C=\{(x,\sum_i x_i^3)\}`$. The conditions $`q\gt 3`$ and $`q\equiv2\pmod3`$ make cubing bijective. Each projection onto $`n-1`$ coordinates is therefore bijective, giving uniform proper marginals. Tensor-product phase gates turn this combinatorial property into an equality of reduced channels, including arbitrary reference systems and arbitrary global inputs.

**Dependencies and story role.** M03, M06, M13, and M14 supply the subsystem, phase, graph, and access language. This milestone introduces the actual pair and establishes the local match before any global summary or computational distinction is used.

**Conceptual connection.** A distribution can hide its defining relation from every proper coordinate marginal while making it apparent in the joint data. The result concerns which coordinates are retained, not whether measurement devices are individually local.

**Sources.** [Watrous §2.1.3 and §4.1.3][watrous]; [graph definitions](../science/model.md#two-phase-distributions); [uniform proper marginals and reduced channels](../science/channels.md#2-equality-of-every-proper-reduced-channel); [two-input illustration](WATROUS_BRIDGE.md#worked-example-two-inputs-over-five-symbols).

<a id="m16"></a>

### M16 — Matched source and channel diagnostics

**Central question.** Which exact matches follow from the common phase-probability multiset, and which need additional structure?

**Understanding target.** Both graph laws are uniform on $`q^{n-1}`$ points. Orthogonality of phase-labelled states yields the same source and normalized Choi spectra, hence the same spectral entropies and minimal environment dimensions. The source diagonal is shared because phase gates do not change computational probabilities. Coherence, bath entropy, fidelity metrics, and unitarity then follow from their stated formulas. Proper reduced-channel equality uses the graph projections from M15, rather than support size alone.

**Dependencies and story role.** M08–M09 organize the diagnostics and M15 supplies the distributions. This milestone collects the common physical quantities before their limits are examined, while avoiding the impression that each scalar match is an independent new mechanism.

**Conceptual connection.** One structural fact can generate many diagnostic equalities. Their joint presence makes the comparison controlled, but it does not recover the full arrangement of eigenvectors relative to the secret encoder.

**Sources.** [Watrous §2.2.2 and §§5.2.1–5.2.2][watrous]; [source spectra](../science/channels.md#3-source-spectra-entropy-and-coherence); [Choi spectra and scalar metrics](../science/channels.md#4-choi-spectra-and-scalar-channel-metrics); [scope of the diagnostic collection](../science/interpretation.md#scope-of-the-contribution).

<a id="m17"></a>

### M17 — Equal capacity and different channel actions

**Central question.** Why does an equal quantum capacity coexist with different fixed sectors and superoperator spectra?

**Understanding target.** The phase-channel complement depends only on the input diagonal, making the channel degradable. Weyl covariance and concavity select the maximally mixed input, giving $`Q=n\log_2q-H(\nu)=\log_2q`$ for both graph laws. This value is not inferred from Choi isospectrality alone. The linear channel preserves exact coherent fibers and is idempotent; the cubic channel has some Fourier multipliers with magnitude strictly between zero and one.

**Dependencies and story role.** M06, M10, M12, and M16 supply operator multipliers, distance, capacity, and the common diagnostics. This milestone identifies the global channel distinctions that remain before the secret-recovery tasks are analyzed.

**Conceptual connection.** An optimized asymptotic code and an exact noiseless subspace are different mechanisms. Matching the communication rate does not force either identical channel action or identical behavior on a prescribed encoded source.

**Sources.** [Watrous §§4.2.2 and 8.2.1–8.2.2][watrous]; [capacity proof](../science/channels.md#5-exact-quantum-capacity); [superoperator and noiseless-sector distinctions](../science/channels.md#62-choi-isospectrality-is-not-channel-unitary-equivalence); [primary capacity sources](../references/RELATED_WORK.md#6-coherence-channel-diagnostics-and-capacity).

<a id="m18"></a>

### M18 — Linear records and coherent fibers

**Central question.** What information remains coherent when the environment records a rank-$`r`$ linear function of the input?

**Understanding target.** Uniform phase noise on a subspace $`W`$ removes matrix elements unless the corresponding inputs have the same record $`Ba`$, where $`B`$ has row space $`W`$. An invertible coordinate change writes the input as a recorded part $`x`$ and an unrecorded fiber coordinate $`y`$. The transformed secret splits correspondingly into $`u`$ and $`v`$. Fourier measurement of the fiber reveals $`v`$ whenever the measured scalar frequency is nonzero.

**Dependencies and story role.** M06 supplies phase orthogonality, M07 the residual learning problem, and M15 the selected hyperplane. This milestone isolates the mechanism behind the hard branch before M19 establishes a reduction for arbitrary quantum processing.

**Conceptual connection.** Macroscopic coherent support can preserve only a limited quotient of the secret. The amount of remaining coherence and the number of residual classical unknowns are related through an exact coordinate decomposition, not a heuristic entropy argument.

**Sources.** [Watrous §§2.2.2, 2.3.1, and 4.1.3][watrous]; [linear-record theorem](../science/hardness.md#theorem-a-fixed-linear-record); [record coordinates](../science/hardness.md#the-record-and-its-coordinates); [complementary secret](../science/hardness.md#learning-the-complementary-secret).

<a id="m19"></a>

### M19 — The exact residual-LWE equivalence

**Central question.** Why can no unrestricted collective learner bypass the hard branch merely by using its remaining coherence?

**Understanding target.** Once the complementary secret is known, a fresh source copy gives an exact classical $`r`$-dimensional LWE sample and a known uniform fiber. Conversely, one classical residual-LWE sample plus a chosen known complementary secret prepares one exact quantum source copy. The simulator preserves the uniform full-secret distribution and uses one classical sample per emitted copy. The selected linear graph leaves $`\kappa=s_n-\sum_{i\lt n}s_i`$ accessible and exactly $`(n-1)`$-dimensional LWE unresolved.

**Dependencies and story role.** M07 fixes the classical-input assumption and M18 gives the fiber decomposition. This milestone completes the hard-side argument as a source simulation, rather than a lower bound limited to one measurement.

**Conceptual connection.** A fixed unknown record can also be identified from its affine Fourier support; withholding that record is not the claimed hardness resource. The remaining difficulty is the stated LWE problem with unchanged modulus and error law.

**Sources.** [Watrous §§2.2.2 and 2.3.1][watrous] supply representation and measurement language; [exact simulator](../science/hardness.md#simulating-quantum-copies-from-classical-lwe), [linear specialization](../science/hardness.md#the-linear-family-in-the-comparison), and [unknown fixed record](../science/hardness.md#a-fixed-unknown-record-can-be-identified) supply the reduction.

<a id="m20"></a>

### M20 — Fourier outcomes and cancellation of label noise

**Central question.** What exact data does the product Fourier measurement expose, and where does the additive error go?

**Understanding target.** The measured pair satisfies $`u=-ks-z`$, with $`k`$ uniform and independent of the phase label. The shared scalar error contributes only the branch phase $`\omega^{ke}`$ before measurement, so it disappears from these outcome probabilities. It remains in the full density operator and in the computational diagonal. For the cubic law, the first $`n-1`$ output coordinates are uniform conditional on every $`k`$, which gives a secret-independent feature distribution.

**Dependencies and story role.** M05–M06 define the measurement and its sign convention; M15 provides the phase supports. This milestone establishes the exact classical statistical model used by the easy learner, without transferring its cancellation property to the hard-side density operator.

**Conceptual connection.** A measurement can remove a nuisance parameter while retaining a different structured noise variable. Here the recoverable information comes from correlations in $`z`$, not from estimating the additive error distribution.

**Sources.** [Watrous §§2.3.1–2.3.2 and 4.1.2][watrous]; [Fourier readout](../science/learning.md#fourier-readout); [error retained in the full state](../science/interpretation.md#the-fourier-measurement-has-equal-single-copy-mutual-information); [Fourier-learning precedents](../references/RELATED_WORK.md#2-noisy-quantum-examples-and-fourier-learning).

<a id="m21"></a>

### M21 — Cubic constraints as linear regression

**Central question.** How does the measured cubic relation reveal all secret coordinates through ordinary modular linear algebra?

**Understanding target.** For $`k\ne0`$, the response $`(u_n-\sum_i u_i^3)/k`$ is linear in the lifted vector $`(s',s'^2,\sum_i s_i^3,s_n)`$. The associated row consists of quadratic monomials in $`u'`$ and $`k`$. There are $`2n`$ lifted coordinates, although the original secret has only $`n`$ coordinates. Once the feature matrix has full column rank, its unique solution yields the secret and automatically satisfies the promised algebraic consistency relations.

**Dependencies and story role.** M13 supplies polynomial lifting and M20 the exact measurement law. This milestone identifies the recovery mechanism; M22 separately controls how many raw emissions suffice to obtain enough independent constraints.

**Conceptual connection.** The nonlinear graph is used as a structured source of coefficients, while the recovery computation after measurement is linear. The result uses established polynomial reconstruction ideas, with its significance located in the simultaneous channel comparison.

**Sources.** [Watrous §2.3.1][watrous] anchors the conversion to classical outcomes; [exact polynomial relation](../science/learning.md#the-exact-polynomial-relation), [algorithm](../science/learning.md#algorithm), and [hidden-polynomial precedents](../references/RELATED_WORK.md#5-hidden-polynomial-graphs-and-interpolation) supply the project-specific algebra.

<a id="m22"></a>

### M22 — A fixed raw-copy recovery guarantee

**Central question.** How is the learner's success guaranteed without hiding discarded outcomes or an unbounded stopping time?

**Understanding target.** Every nonzero linear combination of the features is a nonzero polynomial of degree at most two. Conditional on $`k\ne0`$, its zero probability is bounded on the product grid. Charging the rejected $`k=0`$ outcomes gives a per-raw-copy bound $`3/q`$ for failing to constrain a fixed coefficient direction. Independence and a union bound yield the fixed budget

```math
N=\left\lceil
\frac{2n\ln q+\ln(1/\delta)}{\ln(q/3)}
\right\rceil.
```

**Dependencies and story role.** M13 supplies the polynomial zero bound and M21 the feature system. This milestone makes the ideal learner a finite protocol, enabling the implementation and perturbation bounds in M25.

**Conceptual connection.** Accepted equations and requested quantum copies are different resources. A bound on the latter also controls total exposure to imperfect preparation and readout; no source call is hidden by postselection.

**Sources.** [Watrous §1.2.2 and §2.3.2][watrous]; [fixed raw-copy theorem](../science/learning.md#theorem-a-fixed-raw-copy-budget); [rank-probability proof](../science/learning.md#proof-of-the-copy-bound). The finite-field zero bound and copy formula are proved locally.

<a id="m23"></a>

### M23 — Fixed unknown cubic coefficients

**Central question.** Which uncertainty in the programmed cubic relation can be absorbed into the learner?

**Understanding target.** The proved extension allows fixed unknown nonzero coefficients $`c_i`$ and a fixed offset $`d_0`$ in $`z_n=d_0+\sum_i c_ix_i^3`$. Every proper marginal remains uniform. An unnormalized cubic regression uses all outcomes, including $`k=0`$, and has $`3n`$ lifted coordinates. The recovered products $`c_is_i`$ and nonzero $`c_i`$ determine each $`s_i`$; the remaining coordinates directly identify $`s_n`$ and $`d_0`$.

**Dependencies and story role.** M21–M22 supply lifting and the fixed-copy argument. This milestone records the existing bounded extension before implementation introduces physical uncertainty. It separates parameters fixed across the experiment from noise drawn afresh on every emission.

**Conceptual connection.** Persistent calibration uncertainty can be an identifiable part of the same model. Fresh phase jitter instead creates new errors in the equations; the fixed-parameter theorem does not supply a decoder for that different distribution.

**Sources.** [Watrous §§1.2.2 and 2.3.1][watrous] supply probability and measurement language; [fixed unknown coefficients](../science/learning.md#fixed-unknown-coefficients); [calibration versus fresh phase noise](../science/implementation.md#7-perturbative-success-and-the-regime-not-settled-here). The extended algebra and its raw-copy bound are local proofs.

<a id="m24"></a>

### M24 — A physical source and explicit readout costs

**Central question.** What operations actually prepare and measure the source when arbitrary data loading and unit-cost Fourier transforms are unavailable?

**Understanding target.** The secret holder prepares uniform field registers, samples the scalar error and phase labels, and applies reversible modular arithmetic and known phase rotations. A pairwise finite-bath construction realizes the same correlated channel on a star geometry. The learner's Fourier measurement can use phase estimation of a public modular shift, whose controlled powers are known modular additions. System size, workspace, random bits, gate accuracy, interaction scale, and copy count are all distinct resources.

**Dependencies and story role.** M04 and M06 supply the channel and Fourier descriptions; M19–M20 specify what the simulator and learner require. This milestone connects those abstract maps to the explicit resource accounting that the access contract promises.

**Conceptual connection.** An engineered finite-bath realization demonstrates physical structure without identifying a thermal environment or assuming constant depth. Polynomial digital gate cost also does not imply constant Hamiltonian strength or duration.

**Sources.** [Watrous §2.2.2 and §2.3.1][watrous]; [source preparation](../science/implementation.md#1-source-preparation-without-a-data-loading-oracle); [pairwise baths and strength](../science/implementation.md#2-pairwise-bath-realization); [explicit Fourier readout](../science/implementation.md#3-fourier-readout-with-explicit-arithmetic). Circuit details and their primary sources are local.

<a id="m25"></a>

### M25 — Finite precision for the complete protocol

**Central question.** How accurate must each emission and readout be for the finite-copy recovery claim to remain meaningful?

**Understanding target.** A protocol using $`M`$ raw copies has failure probability at most its ideal failure plus $`M(\varepsilon_{\mathrm{src}}+\varepsilon_{\mathrm{read}})`$. The source error is measured in trace distance and the full readout error in half-diamond distance. Gate-synthesis errors, preparation aborts, and classical sampler errors enter an explicit budget. Independence or a suitable conditional guarantee is required; a collection of marginal promises does not cover arbitrary correlations across emissions.

**Dependencies and story role.** M10 supplies operational distances, M22 a fixed raw-copy count, and M24 an implementable circuit. This milestone converts the ideal learner into a controlled approximation statement before additional physical dephasing is considered.

**Conceptual connection.** Inverse-polynomial per-copy error can suffice for one specified polynomial-copy experiment. A hardness reduction quantified over all polynomial-time adversaries requires negligible simulation error, or an exact reduction for the changed source. Compilation accuracy and uncontrolled noise have different roles.

**Sources.** [Watrous §3.1.1 and §§3.3.2–3.3.3][watrous]; [complete error budget](../science/implementation.md#a-fixed-protocol-has-an-explicit-error-budget); [learner cost and precision](../science/learning.md#cost-and-finite-precision).

<a id="m26"></a>

### M26 — Exact fragility under local dephasing

**Central question.** Why does the local invisibility of the retained coherence also make it fragile to independent dephasing?

**Understanding target.** Uniform proper phase marginals force every surviving nonzero off-diagonal difference to involve all $`n`$ input coordinates. Applying local mixtures $`(1-p_j)\mathrm{id}+p_j\Delta_j`$ therefore multiplies every such term by the same $`\eta=\prod_j(1-p_j)`$. The resulting channel is exactly $`\eta\mathcal D_\nu+(1-\eta)\Delta_A`$. Either additionally dephased source lies at trace distance $`\eta(1-1/q)`$ from the ordinary classical source.

**Dependencies and story role.** M03, M06, M10, M15, and M25 supply subsystems, multipliers, distance, graph marginals, and protocol accounting. This milestone establishes the negative robustness theorem through a channel identity and an explicit simulator.

**Conceptual connection.** Constant local dephasing makes polynomially many emissions exponentially close to classical $`n`$-dimensional LWE. This invokes an $`n`$-LWE assumption, distinct from the ideal linear branch's $`(n-1)`$-LWE equivalence. The same global support property enables the ideal comparison and its fragility.

**Sources.** [Watrous §§2.2.1, 3.1.1, and 4.1.3][watrous]; [product attenuation identity](../science/implementation.md#proposition-5-product-attenuation-identity); [exact distance](../science/implementation.md#corollary-51-exact-distance-from-the-classical-source); [conditional noisy hardness](../science/implementation.md#corollary-52-a-conditional-hardness-regime).

<a id="m27"></a>

### M27 — The matched dephasing trajectory

**Central question.** Which matches survive additional dephasing, and what can their continuous decay establish about recovery?

**Understanding target.** The effective phase law is $`\nu_\eta=\eta\nu+(1-\eta)U`$, with one probability value on the graph and one outside. Its probability multiset remains the same for the two graphs at every common $`\eta`$. Source and Choi spectra, bath entropy, scalar metrics, proper marginals, coherence, and capacity remain matched. Their common capacity and coherence decrease from $`\log_2q`$ to zero, while the complete channel distance contracts by $`\eta`$.

**Dependencies and story role.** M08, M12, M16, and M26 supply the spectral formulas, capacity meaning, original matches, and exact mixture. This milestone connects the ideal endpoint to a fully classical endpoint without inventing an algorithm throughout the interval.

**Conceptual connection.** A perturbative success bound near the ideal source and a hardness reduction near the classical source leave an intermediate regime unresolved. Nonzero capacity or inverse-polynomial distinguishability alone does not classify the best secret-recovery complexity.

**Sources.** [Watrous §§5.2.1–5.2.2 and 8.2.1–8.2.2][watrous]; [matched trajectory formulas](../science/implementation.md#6-matched-spectra-and-capacity-along-the-dephasing-trajectory); [perturbative success and remaining regime](../science/implementation.md#7-perturbative-success-and-the-regime-not-settled-here).

<a id="m28"></a>

### M28 — Single-copy information and many-copy inference

**Central question.** What information is equal in the two experiments, and why does that not settle repeated-secret recovery?

**Understanding target.** For a uniform secret, the actual Fourier measurement has equal single-copy mutual information $`(1-1/q)\log_2q`$ for both graph laws and every additive error law. General Holevo information need not match because the ensemble-average states can differ. With uniform additive errors, all source states commute in the Fourier basis: the linear source identifies only a quotient, while the cubic learner identifies the full secret. With narrow errors, the residual hard secret may still be statistically identifiable by expensive enumeration.

**Dependencies and story role.** M11 supplies the information distinctions, M19 the residual hard problem, and M22 the recovery guarantee. This milestone reconciles the computational theorem with both the information-theoretic endpoint and the finite counterexamples.

**Conceptual connection.** Single-copy information counts uncertainty reduction on average; it does not specify the direction or independence of constraints accumulated under a fixed secret. Statistical sufficiency and efficient decoding remain separate.

**Sources.** [Watrous §§5.1.1, 5.2.1, and 5.3.3][watrous]; [Fourier mutual information](../science/interpretation.md#the-fourier-measurement-has-equal-single-copy-mutual-information); [Holevo examples and error-law limits](../science/interpretation.md#equal-conditional-spectra-do-not-imply-equal-holevo-information).

<a id="m29"></a>

### M29 — What local equivalence and global discrimination imply

**Central question.** Why do neither a local pre-encoding unitary nor an easy channel-discrimination experiment erase the learning separation?

**Understanding target.** A product Fourier-basis relabelling maps the two pre-encoding phase states into one another. Converting the received source by the displayed conjugation also requires the unknown $`U_s`$, so this identity does not give a public source conversion. Separately, product probes and Fourier measurements distinguish the complete phase channels with a constant advantage by processing all labels jointly. Their half-diamond distance is the total-variation distance of their phase laws.

**Dependencies and story role.** M10, M15, M17, M19, and M28 distinguish channel distance, marginal equality, non-equivalent actions, computational simulation, and ensemble information. This milestone resolves two apparent shortcuts before the final synthesis.

**Conceptual connection.** Knowing which public noise law is present is different from recovering the secret encoded beneath it. Proper-subsystem equality also supplies no general lower bound on tomography using product measurements and joint classical processing.

**Sources.** [Watrous §§2.2.2, 3.3.1–3.3.2, and 4.2.2][watrous]; [secret-dependent conversion](../science/interpretation.md#a-local-equivalence-before-encoding-is-not-a-source-conversion); [complete channel distance](../science/channels.md#61-the-complete-channels-are-separated-in-diamond-norm); [global discrimination scope](../science/interpretation.md#local-invisibility-does-not-prevent-global-channel-discrimination).

<a id="m30"></a>

### M30 — Global synthesis: the conditional separation and its scope

**Central question.** What complete conclusion is supported when the matched diagnostics, reductions, algorithm, and physical limits are assembled?

**Understanding target.** The project compares two explicit, public, secret-independent correlated phase laws under one state-copy contract. Their stated local and scalar diagnostics match. The ideal linear source is exactly equivalent to residual classical-input LWE, while the cubic source has a finite-copy polynomial-time learner. The computational separation is conditional on the selected LWE family. Independent local dephasing has an exact classical-source limit, and the intervening recovery complexity is not fully classified.

**Dependencies and story role.** M14 provides the initial pipeline; M15–M29 supply its complete scientific narrative. This final synthesis locates each conclusion at its proper level: unconditional identity, explicit algorithm, computational assumption, resource construction, numerical check, or unresolved comparison.

**Conceptual connection.** The result limits what the specified collection of channel diagnostics predicts about one inference task. It establishes neither an ordinary public-key attack, a general equal-Holevo theorem, a constant-noise learner, nor an unqualified priority claim.

**Sources.** [Watrous §§2.2, 3.3, 5.3.3, and 8.2][watrous]; [main theorem](../science/model.md#main-theorem); [scope](../science/interpretation.md#scope-of-the-contribution); [related-work coverage](../references/RELATED_WORK.md#9-version-and-coverage-notes); [finite verification](../verification/README.md). Canonical science pages remain the authoritative proofs.

[watrous]: https://jhwatrous.github.io/TQI.pdf
[watrous-page]: https://jhwatrous.github.io/books-and-courses.html
