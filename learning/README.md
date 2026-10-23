# Learning LWE Noise Geometry

The learning route develops one question: **why can noise channels with matching local action and many matching global diagnostics leave different computational learning problems?** Its endpoint is the precise linear/cubic separation, including the source it requires and the independent dephasing that removes its advantage.

## Three complementary entry points

| Entry point | Use it for |
|---|---|
| [30 milestones](MILESTONES.md) | Follow the project's logical dependencies, from elementary representations to the complete result and its limits. |
| [Watrous bridge](WATROUS_BRIDGE.md) | Read the relevant textbook sections, translate notation, and connect them to a fully worked finite-field example. |
| [Scientific account](../science/README.md) | Read the exact definitions, statements, proofs, resource costs, and interpretation directly. |

The map and bridge explain how the scientific pieces fit together. The topic pages under `science/` remain the authoritative homes of the proofs.

## The single educational anchor

**John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018.** The author provides the [book and chapter links](https://jhwatrous.github.io/books-and-courses.html) and a [prepublication manuscript](https://jhwatrous.github.io/TQI.pdf).

The [bridge](WATROUS_BRIDGE.md) specifies the sections used and translates their conventions. The central foundations are density operators, channels and their representations, distinguishability, mixed-unitary and Schur channels, entropy, and quantum capacity. Finite-field polynomial learning, the exact LWE simulator, and the source-access contract are supplied by this repository and its cited research. The book is not assigned in full.

## The two phases

| Phase | Milestones | Scientific purpose |
|---|---|---|
| Background and preliminaries | M01–M14 | Build the register, channel, information, computational, and algebraic language, then assemble a single consistent description of the source. |
| Narrative and innovation | M15–M30 | Construct the graph pair; prove the matching and differing properties; follow the hard and easy learning branches; account for implementation, dephasing, and information; synthesize the contribution. |

Both phases move from individual objects and calculations toward the complete system. Dependencies and conceptual connections in each milestone explain why the next step is needed. M14 and M30 are synthesis points.

For a first pass, follow the milestone order and read the linked bridge passage before the corresponding scientific proof. For a focused question, use the [science guide's question index](../science/README.md#follow-a-question) and the milestone dependencies to identify the required background.

## Keep the scientific distinctions visible

The source holder knows the secret; the learner receives independent copies of an emitted quantum state. That interface is part of the theorem. A computational-basis measurement gives ordinary LWE, but ordinary public LWE samples do not provide this coherent source.

The ideal linear branch reduces exactly to `(n−1)`-dimensional classical-input LWE. The additional-dephasing argument uses `n`-dimensional LWE. Hardness is conditional; the channel identities, reductions, and cubic recovery algorithm have explicit proofs.

Matching per-secret spectra is not equality of the ensemble's Holevo information. Matching quantum capacity is not equality of computational learning difficulty. Proper-marginal equality concerns subsets of the noisy input registers. The [interpretation](../science/interpretation.md) explains these distinctions and the information counterexamples.

## Check an example and then the general result

The [bridge](WATROUS_BRIDGE.md) contains a complete small example of the channel geometry and cubic recovery. It illustrates the algebra; the fixed raw-copy guarantee is proved in [Secret recovery](../science/learning.md).

The [verification guide](../verification/README.md) documents executable finite checks, parameter cases, numerical tolerances, and stored results. These checks complement the proofs. They do not establish cryptographic hardness or priority.
