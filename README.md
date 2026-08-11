# Liquid Neural Networks from First Principles

A systematic, long-term research-learning repository for understanding, deriving, implementing, and reproducing Liquid Neural Networks from first principles.

## Project Goal

This repository is **not** a shallow demo or a thin wrapper around the `ncps` library. Its goal is to build a complete, first-principles understanding of Liquid Neural Networks through:

- A 6-part, 20-stage structured curriculum
- A continuously maintained LaTeX textbook
- Pure PyTorch implementations of every core architecture
- Unified experiment and benchmark infrastructure
- A historical timeline tracing the algorithm evolution

## Prerequisites

### Required

- **Linear Algebra**: vectors, matrices, eigenvalues/eigenvectors
- **Multivariable Calculus**: derivatives, partial derivatives, chain rule, basic integration
- **Deep Learning**: MLP, backpropagation, activation functions, optimization, basic RNN/LSTM concepts
- **PyTorch**: tensors, autograd, `nn.Module`, optimizers, training loops

### Not Required (provided by this curriculum)

- Prior knowledge of ODEs
- Dynamical systems theory
- Numerical analysis
- Control theory

These foundations are taught within the repository as they become necessary.

## Learning Philosophy

- **First principles** — understand the mathematics before touching code
- **Derive before implement** — write the derivation before typing the forward pass
- **Implement before relying on libraries** — clean-room implementations verified against reference code
- **Experiments validate theory** — every theoretical claim gets a numerical check
- **Notes consolidate understanding** — LaTeX notes lock in the learning

## Repository Structure

```text
src/lnn/             Pure PyTorch implementations (ode, rnn, ltc, cfc, ssm, ...)
tests/               pytest unit tests per module
experiments/         Unified benchmarks (foundations, dynamics, timeseries, ...)
notes/               LaTeX textbook (chapters, references, figures)
learning/            Curriculum state, paper log, decisions, questions
reference/           Timeline, notation reference sheets
```

## Getting Started

```bash
pip install -e ".[dev]"
pytest
ruff check src/
```

Start reading at `learning/curriculum.md` and `learning/current_stage.md`.

## Reference Implementations

The following libraries are used only as correctness oracles, never as substitutes for our own clean-room implementations:

- `torchdiffeq` — Neural ODE solver reference
- `ncps` — NCP / LTC / CfC reference
- Original author code repositories (LTC, CfC, Liquid-S4, LRC, LrcSSM)

## License

MIT
