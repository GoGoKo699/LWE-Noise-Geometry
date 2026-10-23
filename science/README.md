# Scientific account

The project asks whether matching local noise action and major scalar channel diagnostics determines how difficult it is to learn a secret from a coherent source. An explicit linear/cubic pair shows that it does not, under a stated classical-input LWE hardness assumption. The same construction yields an exact account of why independent local dephasing destroys the advantage.

## Read in order

1. [Source model and separation theorem](model.md) defines every register, access restriction, parameter, and main claim.
2. [Channel invariants](channels.md) proves the matching local marginals, source and Choi spectra, coherence, fidelities, unitarity, and capacity, and identifies the channel properties that differ.
3. [Hardness](hardness.md) gives the exact equivalence between the linear branch and lower-dimensional classical-input LWE.
4. [Learning](learning.md) derives the cubic learner and its finite raw-copy guarantee.
5. [Implementation and perturbations](implementation.md) accounts for the physical source, computational resources, approximation error, and independent-dephasing fragility.
6. [Interpretation](interpretation.md) explains information versus computation, the role of source access, and the limits of the comparison.

## Follow a question

| Question | Start here |
|---|---|
| What extra resource does the learner receive? | [Access contract](model.md#access-contract) |
| Which quantities are exactly equal? | [Channel invariants](channels.md) |
| Could a collective quantum attack evade the hard-side proof? | [Hardness](hardness.md) |
| How many actual emitted copies does the learner need? | [Learning](learning.md) |
| What happens under independent noise on each input register? | [Implementation and perturbations](implementation.md) |
| Is the single-copy information the same? | [Interpretation](interpretation.md#the-fourier-measurement-has-equal-single-copy-mutual-information) |
| What is inherited from earlier work? | [Related work](../references/RELATED_WORK.md) |
| Which identities can be checked on finite instances? | [Verification](../verification/README.md) |

The mathematical proofs are authoritative for general parameters. Numerical checks cover stated finite cases; they do not prove the cryptographic assumption or establish priority.

## Build the prerequisites

The [learning guide](../learning/README.md) connects this account to a [30-milestone map](../learning/MILESTONES.md) and the [Watrous bridge](../learning/WATROUS_BRIDGE.md). The bridge introduces the channel language and finite-field calculations used here; each milestone points back to the canonical scientific statement or proof.
