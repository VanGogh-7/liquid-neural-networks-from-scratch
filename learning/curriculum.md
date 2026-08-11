# Curriculum — Liquid Neural Networks from First Principles

## Stage Phase Profiles

The learning lifecycle is `READ → EXPLAIN → DERIVE → QUESTION → LEARNED`. The repository lifecycle is `HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE`. The table explicitly defines which phases apply to each Stage. Applicable phases remain ordered and cannot be skipped by default. Every `N/A` entry includes its reason.

| Stage | Learning phases | Repository phases | N/A phases and reasons |
| --- | --- | --- | --- |
| 00 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → WRITE → REVIEW → DONE | IMPLEMENT: no algorithm or software component is built. TEST: no executable numerical behavior exists. EXPERIMENT: notation policy has no empirical claim. |
| 01 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → EXPERIMENT → WRITE → REVIEW → DONE | IMPLEMENT: the Stage establishes ODE concepts rather than a reusable solver. TEST: no reusable implementation is produced. |
| 02 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → EXPERIMENT → WRITE → REVIEW → DONE | IMPLEMENT: the Stage develops dynamical-systems analysis rather than a library component. TEST: numerical illustrations are reviewed as experiments, not software tests. |
| 03 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 04 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 05 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 06 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 07 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → WRITE → REVIEW → DONE | IMPLEMENT: implementation belongs to Stage 08. TEST: there is no Stage 07 software artifact. EXPERIMENT: numerical LTC studies begin after the Stage 08 implementation. |
| 08 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 09 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 10 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → WRITE → REVIEW → DONE | IMPLEMENT: implementation belongs to Stage 11. TEST: there is no Stage 10 software artifact. EXPERIMENT: CfC benchmarking begins after the Stage 11 implementation. |
| 11 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 12 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 13 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 14 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 15 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 16 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 17 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 18 | READ → EXPLAIN → DERIVE → QUESTION → LEARNED | HANDOFF → INTEGRATE → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE | None. |
| 19 | READ → EXPLAIN → QUESTION → LEARNED | HANDOFF → INTEGRATE → EXPERIMENT → WRITE → REVIEW → DONE | DERIVE: no single frontier model is mandatory. IMPLEMENT and TEST: the survey has no fixed software deliverable. If a specific reproduction is selected, amend this profile and record the decision first. |

## PART I — Mathematical & Continuous-Time Foundations

### Stage 00 — Mathematical Language and Notation

- **Objective**: Establish a unified mathematical notation and tensor-shape convention used throughout the entire curriculum.
- **Prerequisites**: Basic familiarity with linear algebra, calculus, and PyTorch tensors.
- **Core Topics**:
  - Scalars, vectors, matrices
  - Functions and mappings
  - Derivatives, partial derivatives, gradient, Jacobian, Hessian
  - Norms
  - Eigenvalues and eigenvectors
  - Element-wise operations
  - Continuous and sampled time notation ($t$, $k$, $t_k$, $\Delta t_k$)
  - Column-vector, gradient, and Jacobian conventions
  - Batch-first tensor shapes `(B, T, D)` and state shapes `(B, D)`
  - Time-first ODE callables: `f(t, x)` and `f(t, x, u)`
  - Paper-notation-to-repository-notation translation
  - Numerical precision policy
  - Mathematical notation ↔ PyTorch tensor mapping
- **Implementation Goal**: N/A — Stage 00 defines language and documentation, not an algorithm or software component.
- **Experiment Goal**: N/A — notation conventions do not make an empirical claim.
- **Writing Goal**: Create and review the `notation` and `tensor_shapes` reference sheets, including worked math-to-PyTorch shape mappings.
- **Exit Criteria**:
  - Can read any formula in the curriculum without notation ambiguity
  - Can map any mathematical vector/matrix to its PyTorch tensor shape
  - Notation reference sheet is complete and consistent

### Stage 01 — ODE Essentials

- **Objective**: Learn the minimum ODE theory needed to read Neural ODE, LTC, CfC, and SSM papers.
- **Prerequisites**: Stage 00, multivariable calculus.
- **Core Topics**:
  - What is an ODE? State, time, vector fields, trajectories
  - Initial value problems
  - Autonomous vs. non-autonomous systems
  - External inputs / controlled dynamics
  - Exponential decay: $\dot{x} = -\lambda x$
  - First-order linear ODE, time constants
  - Linear ODE systems, matrix exponential
  - Existence and uniqueness, Lipschitz condition (intuition)
- **Implementation Goal**: None (theory stage).
- **Experiment Goal**: Manually plot and explore exponential decay, linear ODE solutions.
- **Exit Criteria**:
  - Can explain why $x(t)$ is a trajectory
  - Can explain why an ODE defines a vector field
  - Understands what an initial condition is
  - Can explain why $\tau$ is called a time constant and how its magnitude affects system response

### Stage 02 — Dynamical Systems

- **Objective**: Build the stability and phase-portrait intuition needed for LNN analysis.
- **Prerequisites**: Stage 01.
- **Core Topics**:
  - State space, flow
  - Equilibrium points
  - Stability, asymptotic stability
  - Boundedness
  - Phase portraits
  - Jacobian linearization
  - Eigenvalue stability (linear algebra → eigenvalues → stability)
- **Implementation Goal**: None (theory stage).
- **Experiment Goal**: Plot phase portraits for 2D linear systems; verify stability predictions numerically.
- **Exit Criteria**:
  - Can classify equilibria from eigenvalues
  - Can sketch a phase portrait for a 2D linear system
  - Understands the linear algebra → dynamical stability bridge

### Stage 03 — Numerical ODE Solvers

- **Objective**: Implement and understand numerical ODE solvers from Taylor expansions.
- **Prerequisites**: Stage 01.
- **Core Topics**:
  - Why numerical solvers?
  - Taylor expansion → Forward Euler (derivation required)
  - Local truncation error, global error
  - Step size effects
  - Heun's method (RK2)
  - RK4
  - Adaptive solvers (concept)
  - Stiffness, numerical stability
  - Differentiable solvers
- **Implementation Goal**: Implement `Euler`, `Heun`, and `RK4` in `src/lnn/ode/`; write convergence tests.
- **Experiment Goal**: Exponential decay, harmonic oscillator, solver error convergence, step-size effects, simple stiff system.
- **Exit Criteria**:
  - Can derive Euler from Taylor expansion
  - Can implement Euler, Heun, RK4 from scratch
  - Can explain local vs. global error
  - Can describe stiffness and its implications

---

## PART II — Continuous-Time Neural Networks

### Stage 04 — Continuous-Time RNN

- **Objective**: Bridge discrete RNNs to continuous-time dynamics.
- **Prerequisites**: Stage 01, Stage 03, basic RNN knowledge.
- **Core Topics**:
  - Discrete RNN ↔ continuous-time dynamics relationship
  - Leak term, fixed time constant
  - CT-RNN formulation: $\tau \dot{\mathbf{h}} = -\mathbf{h} + \phi(\mathbf{W}\mathbf{h} + \mathbf{U}\mathbf{x} + \mathbf{b})$
  - Discretization schemes
  - Recurrent dynamics and gradient behavior
- **Implementation Goal**: Implement `VanillaRNN` reference and `CTRNNCell` / `CTRNN` in `src/lnn/rnn/`.
- **Experiment Goal**: Compare discrete RNN vs. CT-RNN on simple sequence tasks; study time-constant effects.
- **Exit Criteria**:
  - Can derive the discretized CT-RNN update
  - Understands the role of the leak term
  - Can implement a working CT-RNN

### Stage 05 — Neural ODE

- **Objective**: Understand and implement Neural ODEs with adjoint-based training.
- **Prerequisites**: Stage 03, Stage 04.
- **Core Topics**:
  - $\frac{d\mathbf{h}}{dt} = f_\theta(\mathbf{h}(t), t)$
  - Differentiable ODE solvers
  - Direct backpropagation vs. adjoint method
  - Solver tolerance, NFE (number of function evaluations)
  - Continuous-depth interpretation
- **Implementation Goal**: Minimal Neural ODE using self-implemented Euler/RK4; compare with `torchdiffeq` as reference.
- **Experiment Goal**: Train a Neural ODE on a simple regression/classification task; analyze NFE vs. accuracy.
- **Exit Criteria**:
  - Understands the adjoint method conceptually
  - Can implement a minimal Neural ODE
  - Can explain the continuous-depth viewpoint

---

## PART III — Birth of Liquid Neural Networks

### Stage 06 — Neural Circuit Policies (NCP)

- **Objective**: Understand biologically-inspired sparse wiring and NCP topology.
- **Prerequisites**: Stage 04.
- **Core Topics**:
  - Biological motivation (C. elegans connectome)
  - Sensory → interneuron → command → motor wiring
  - Synapse polarity (excitatory/inhibitory)
  - Structured sparsity
  - Interpretability
  - Random, fully-connected, NCP, and AutoNCP wiring
- **Implementation Goal**: Wiring infrastructure in `src/lnn/ncp/`; network topology visualization.
- **Experiment Goal**: Visualize and compare different wiring patterns.
- **Exit Criteria**:
  - Can explain the NCP wiring hierarchy
  - Can generate and visualize NCP-style sparse connectivity

### Stage 07 — LTC Foundations (Theory)

- **Objective**: Derive Liquid Time-Constant dynamics from circuit principles.
- **Prerequisites**: Stage 04, Stage 06.
- **Core Topics**:
  - Membrane potential, leak conductance
  - Synaptic conductance, reversal potential
  - Chemical synapses
  - Input/state-dependent time constant
  - From $\tau \dot{\mathbf{x}} = -\mathbf{x} + f(\mathbf{x}, \mathbf{u})$ to liquid dynamics
  - Paper-guided derivation (not code-reading)
- **Implementation Goal**: None (theory stage — derive before implementing).
- **Experiment Goal**: None.
- **Exit Criteria**:
  - Can derive the LTC dynamics from the electrical equivalent circuit
  - Can explain why the time constant is "liquid" (input/state-dependent)
  - Can write the full LTC ODE system

### Stage 08 — LTC Implementation

- **Objective**: Implement LTC from scratch in pure PyTorch.
- **Prerequisites**: Stage 07.
- **Core Topics**:
  - `LTCCell`, `LTC` module
  - Sensory synapses, recurrent synapses
  - Conductance, reversal potential, leak dynamics
  - ODE unfolding (Euler, RK-style, semi-implicit)
  - Unfold steps, step size, stability, accuracy vs. speed
  - Constraints on parameters
- **Implementation Goal**: Pure PyTorch `LTCCell` and `LTC`; compare against `ncps` as oracle.
- **Experiment Goal**: Shape tests, gradient tests, solver convergence, bounded state, batch behavior, irregular `dt`.
- **Exit Criteria**:
  - Full LTC implementation passes all tests
  - Numerical behavior matches reference within tolerance
  - Can explain trade-offs between solver choice, unfold steps, and accuracy

### Stage 09 — LTC Theory

- **Objective**: Study and verify the theoretical properties of LTCs.
- **Prerequisites**: Stage 08, Stage 02.
- **Core Topics**:
  - Stability proofs
  - Boundedness guarantees
  - Expressivity / universal approximation
  - Trajectory behavior under varying time constants
  - Theory ↔ experiment correspondence
- **Implementation Goal**: Numerical verification scripts for each theoretical claim.
- **Experiment Goal**: Verify boundedness, stability regimes, and expressivity claims numerically.
- **Exit Criteria**:
  - Can state and sketch proofs for LTC stability/boundedness
  - Can reproduce key theoretical claims numerically

---

## PART IV — Closed-Form Liquid Networks

### Stage 10 — CfC Theory

- **Objective**: Derive the closed-form approximation that eliminates the ODE solver.
- **Prerequisites**: Stage 08.
- **Core Topics**:
  - Why LTC/Neural ODE need numerical solvers
  - Closed-form solution derivation (paper-guided, self-derived)
  - Gating mechanism
  - Time dependence in the closed form
  - Irregular sampling properties
- **Implementation Goal**: None (theory stage — derive first).
- **Experiment Goal**: None.
- **Exit Criteria**:
  - Can derive the CfC update from the LTC ODE
  - Understands the approximation and its error bounds
  - Can explain the gating structure

### Stage 11 — CfC Implementation

- **Objective**: Implement CfC in pure PyTorch and benchmark against all prior models.
- **Prerequisites**: Stage 10.
- **Core Topics**:
  - `CfCCell`, `CfC`, `WiredCfC`
  - Implementation modes: default, pure, no-gate
  - Unified benchmark: RNN, GRU, LSTM, CT-RNN, Neural ODE, LTC, CfC
  - Metrics: parameters, accuracy, training speed, inference speed, memory, irregular sampling, OOD behavior
- **Implementation Goal**: Pure PyTorch CfC; unified benchmark infrastructure.
- **Experiment Goal**: Full model comparison on multiple task types.
- **Exit Criteria**:
  - CfC implementation passes all tests
  - Benchmark results are reproducible
  - Can explain CfC's speed advantage over LTC

---

## PART V — Liquid State-Space Models

### Stage 12 — State-Space Models

- **Objective**: Understand continuous-time linear SSMs and their discretization.
- **Prerequisites**: Stage 01, Stage 03.
- **Core Topics**:
  - Continuous SSM: $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$, $\mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$
  - Discretization (ZOH, bilinear)
  - State transition, matrix exponential
  - Recurrent view vs. convolution view
  - Long-range dependency
- **Implementation Goal**: Minimal linear SSM in `src/lnn/ssm/`.
- **Experiment Goal**: Sequence copying, long-range memory tasks.
- **Exit Criteria**:
  - Can discretize a continuous SSM
  - Understands recurrent and convolutional representations
  - Can implement a basic linear SSM

### Stage 13 — S4

- **Objective**: Understand structured state-space models (S4).
- **Prerequisites**: Stage 12.
- **Core Topics**:
  - HiPPO matrix (intuition, not full theory)
  - Structured state matrix
  - Diagonal plus low-rank parameterization
  - Efficient recurrent/convolution forms
  - Long-sequence modeling
- **Implementation Goal**: Educational minimal S4.
- **Experiment Goal**: Long-range arena subset; compare with baseline SSM.
- **Exit Criteria**:
  - Understands HiPPO's motivation
  - Can explain S4's efficiency advantage
  - Has a working educational S4

### Stage 14 — Liquid-S4

- **Objective**: Integrate liquid dynamics with structured SSMs.
- **Prerequisites**: Stage 08, Stage 13.
- **Core Topics**:
  - LTC-informed S4 dynamics
  - Input-dependent state transition
  - Liquid-S4 formulation: $\dot{\mathbf{x}} = (\mathbf{A} + \mathbf{B}\mathbf{u})\mathbf{x} + \mathbf{B}\mathbf{u}$
  - Comparison with S4, LSTM, CfC
- **Implementation Goal**: Minimal Liquid-S4.
- **Experiment Goal**: Unified experiment vs. S4, LSTM, CfC.
- **Exit Criteria**:
  - Can derive Liquid-S4 from LTC + S4 principles
  - Understands how liquid dynamics enhance long-range modeling

---

## PART VI — Modern Liquid Architectures

### Stage 15 — STC (Saturated Liquid Time-Constant Networks)

- **Objective**: Understand saturation in synaptic channels.
- **Prerequisites**: Stage 08.
- **Core Topics**:
  - Saturation: sigmoid/tanh gating on conductances
  - STC vs. LTC differences
  - Stability and stiffness implications
- **Implementation Goal**: `STCCell`, `STC` in `src/lnn/stc/`.
- **Experiment Goal**: Compare STC with LTC on dynamics benchmarks.
- **Exit Criteria**:
  - Can explain why saturation matters
  - Can implement STC

### Stage 16 — LRC (Liquid Resistance-Capacitance Networks)

- **Objective**: Understand state-dependent membrane capacitance.
- **Prerequisites**: Stage 15.
- **Core Topics**:
  - Liquid resistance and liquid capacitance
  - Dynamic time-scale control
  - Biological plausibility improvements over LTC/STC
  - Oscillation dampening
- **Implementation Goal**: LRC in `src/lnn/lrc/`.
- **Experiment Goal**: Compare LRC with LTC and STC.
- **Exit Criteria**:
  - Can explain the capacitance term's role
  - Can implement LRC

### Stage 17 — LRCU (LRC Units)

- **Objective**: Build an efficient gated recurrent unit from LRC.
- **Prerequisites**: Stage 16.
- **Core Topics**:
  - Single-step Euler unfolding of LRC
  - Gated RNN structure emerging from LRC discretization
  - Comparison with GRU, LTC, CfC
- **Implementation Goal**: `LRCUCell`, `LRCU` in `src/lnn/lrcu/`.
- **Experiment Goal**: Efficiency benchmark vs. GRU, LTC, CfC.
- **Exit Criteria**:
  - Can derive LRCU from LRC + single-step Euler
  - Can implement and benchmark LRCU

### Stage 18 — LrcSSM

- **Objective**: Scale liquid dynamics to long sequences with parallel scan.
- **Prerequisites**: Stage 17, Stage 14.
- **Core Topics**:
  - Diagonal Jacobian constraint → parallel scan
  - Prefix scan algorithm
  - Sequential vs. parallel computation
  - $\mathcal{O}(T D)$ time/memory, $\mathcal{O}(\log T)$ sequential depth
  - Long-range modeling at scale
- **Implementation Goal**: Sequential LrcSSM and parallel/scan version in `src/lnn/lrcssm/`; educational prefix scan.
- **Experiment Goal**: Long-range benchmarks; speed comparison sequential vs. parallel.
- **Exit Criteria**:
  - Can explain the diagonal Jacobian trick
  - Can implement a prefix scan
  - Has working sequential and parallel LrcSSM

### Stage 19 — Frontiers

- **Objective**: Survey active research directions and recent developments (2025–2026+).
- **Prerequisites**: All prior Stages.
- **Core Topics**:
  - Synaptic activation variants
  - Dual liquid dynamics
  - Emerging architectures
  - Interpretability advances
  - Scalable liquid models
  - Downstream applications: Liquid-GNN, Liquid-CNN, domain-specific Liquid models (appendix only)
- **Implementation Goal**: None (survey stage).
- **Experiment Goal**: Reproduce or analyze results from frontier papers as they appear.
- **Exit Criteria**:
  - Can place new Liquid Network papers in the historical trajectory
  - Understands active open problems
