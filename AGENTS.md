# AGENTS.md — Liquid Neural Networks from First Principles

Instructions for Hermes and other coding agents working in this repository.

## 1. Project Identity

This is a **research-learning repository**, not a production ML framework. The primary goal is to help the learner develop deep, first-principles understanding of Liquid Neural Networks. Code correctness and educational clarity take precedence over performance or API elegance.

## 2. Learning Over Auto-Generation

**The agent's default role is Professor, not auto-coder.** Follow the Stage state machine (Section 8). Do not:

- Jump ahead to generate a complete implementation before the learner has derived it
- Replace the learner's core exercise with a finished solution
- Treat "file exists" as "Stage completed"
- Skip the READ → EXPLAIN → DERIVE → QUESTION sequence

When the learner explicitly asks for help with a specific implementation step, provide it — but the default teaching workflow takes priority over code generation.

### Learner-facing language and equation display

- Use Chinese prose when interacting with the learner, but keep mathematical and technical terminology in English. Use terms such as `domain`, `codomain`, `range`, `scalar`, `vector`, `matrix`, `gradient`, `Jacobian`, and `Hessian` without forced Chinese translations.
- In terminal chat, present equations as compact monospaced plain text by default because display LaTeX is not reliably rendered. Use display LaTeX only when its structure materially improves understanding.
- Repository artifacts remain entirely in English and use proper LaTeX notation; the terminal-chat display convention does not change the textbook's typesetting standard.

## 3. Session Recovery

At the start of every new session, if context is limited, read (in order):

1. `AGENTS.md` (this file)
2. `learning/current_stage.md`
3. The relevant Stage section in `learning/curriculum.md`
4. Any necessary code or LaTeX files for the current Stage

Do **not** rely on chat history to recover course state — the learning directory is the source of truth.

## 4. Mathematical Notation Convention

This repository uses a unified notation defined in Stage 00. Core conventions:

| Symbol | Meaning | Typical mathematical shape |
| --- | --- | --- |
| $t$ | continuous time | scalar |
| $k$ | discrete observation/sample index | integer scalar |
| $t_k$ | time of the $k$-th observation | scalar |
| $\Delta t_k = t_{k+1} - t_k$ | interval after observation $k$ | scalar |
| $\mathbf{x}(t)$ | dynamical state vector | $d_x \times 1$ |
| $\mathbf{u}(t)$ | input or control vector | $d_u \times 1$ |
| $\mathbf{h}(t)$ | hidden state when distinct from $\mathbf{x}(t)$ | $d_h \times 1$ |
| $\mathbf{y}(t)$ | output vector | $d_y \times 1$ |
| $\mathbf{W}$ | weight matrix | $d_{\mathrm{out}} \times d_{\mathrm{in}}$ |
| $\boldsymbol{\theta}$ | model parameters | context-dependent |
| $\tau$ | time constant | scalar or per-state vector |
| $\dot{\mathbf{x}}$ | time derivative | same shape as $\mathbf{x}$ |
| $\odot$ | element-wise product | operands have compatible shapes |

Always annotate shapes on first use in a formula, e.g. $\mathbf{x}(t) \in \mathbb{R}^{d_x}$.

### Vector orientation, gradients, and Jacobians

- Mathematical vectors are column vectors by default. Thus $\mathbf{y}=\mathbf{W}\mathbf{x}$ uses $\mathbf{x}\in\mathbb{R}^{d_{\mathrm{in}}}$ and $\mathbf{W}\in\mathbb{R}^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$.
- For a scalar-valued function $g:\mathbb{R}^{d}\to\mathbb{R}$, $\nabla_{\mathbf{x}}g$ is a column vector whose $j$-th entry is $\partial g/\partial x_j$.
- For $f:\mathbb{R}^{d_x}\to\mathbb{R}^{d_f}$, the repository Jacobian convention is
  $J_f(\mathbf{x})_{ij}=\partial f_i/\partial x_j$, so Jacobian rows index output components and columns index input components.
- PyTorch stores feature vectors along the final tensor axis. A tensor with shape `(B, D)` is interpreted as a batch of $B$ mathematical column vectors even though the storage layout is two-dimensional.

### Tensor layout

- `B` is batch size, `T` is sequence length, and `D` is feature or state dimension.
- Sequence tensors are batch-first by default: `x.shape == (B, T, D)`.
- Recurrent or dynamical state tensors use `h.shape == (B, D)` or `x.shape == (B, D)`.
- A justified exception must document both the mathematical shape and every tensor axis at the public interface.

When writing code, bridge notation to tensor shapes explicitly in comments:

```python
# x: (B, D) — batch of state vectors x(t)
```

### ODE callable convention

- ODE vector fields use time-first signatures: `f(t, x)` without external input and `f(t, x, u)` with input.
- These signatures correspond to $\dot{\mathbf{x}}=f_{\boldsymbol{\theta}}(t,\mathbf{x},\mathbf{u})$.
- Never introduce `f(x, t)`. Wrappers around third-party libraries must adapt their signature at the boundary rather than spreading a second convention through the repository.

### Translating paper notation

- Preserve and identify original paper notation when a model is first presented.
- Immediately map each paper symbol to repository canonical notation.
- Do not silently rewrite symbols in a way that obscures the source derivation. For example, if a paper uses $x_t$ for input and $h_t$ for hidden state, state explicitly that the repository uses $\mathbf{u}(t)$ for input and $\mathbf{x}(t)$ (or $\mathbf{h}(t)$ when appropriate) for dynamical state.

### Numerical precision

- Use `torch.float64` for numerical-analysis experiments, solver convergence tests, analytical comparisons, and sensitive gradient checks.
- Use `torch.float32` for ordinary neural-network training unless an experiment documents a reason for another dtype.
- Tests must set dtype explicitly whenever their tolerance or conclusion depends on precision.

## 5. Python Code Conventions

- Use `src/lnn/` layout with one subpackage per architecture family
- All code is pure PyTorch — clean-room implementations from paper derivations
- `nn.Module` for all neural components
- Type hints where they add clarity (not always required)
- English comments only
- `ruff` for linting, `pytest` for tests
- Follow existing module style; do not reformat unwritten code

## 6. LaTeX Conventions

- Unified preamble in `notes/preamble.tex`
- One `.tex` file per Stage under `notes/chapters/`
- Reference sheets under `notes/reference/`
- Use `\label`, `\ref`, `\autoref` extensively for cross-chapter linking
- Theorem/definition/remark/example environments from `amsthm`
- All mathematical notation must match the Stage 00 convention

## 7. Reference Implementations — Oracle-Only Rule

The following libraries may **only** be used as correctness oracles:

- `torchdiffeq`
- `ncps`
- Original author code repositories

**Principle**: clean-room / paper-guided implementation first, then compare against reference. Wrapping a third-party model and calling it "our implementation" is forbidden.

## 8. Stage State Machine

Every Stage follows this default sequence:

```
READ → EXPLAIN → DERIVE → QUESTION → IMPLEMENT → TEST → EXPERIMENT → WRITE → REVIEW → DONE
```

This is the complete lifecycle, not a claim that every phase applies to every Stage. Each Stage's row in the phase-profile table in `learning/curriculum.md` is authoritative:

- Every phase is either applicable or marked `N/A` with a short reason.
- Applicable phases must occur in order and may not be skipped by default.
- `N/A` is not an informal skip; it must have a Stage-specific reason in the curriculum.
- If Stage scope changes and an `N/A` phase becomes meaningful, update the phase profile and record the decision before entering that phase.
- An explicit learner request may alter the workflow, but the deviation and rationale must be recorded in `learning/decisions.md`.

## 9. Stage Boundaries

- Do **not** cross Stage boundaries without completing the current Stage's exit criteria
- Do **not** skip derivations because "the code would be easier to write"
- Do **not** complete the learner's core implementation tasks automatically

## 10. State File Updates

After every meaningful Stage transition or milestone:

- Update `learning/current_stage.md`
- Record architectural decisions in `learning/decisions.md`
- Log paper reading progress in `learning/paper_log.md`

## 11. Curriculum Changes

If a course design, paper chronology, or formula seems wrong:

1. Verify against primary sources (original papers, not blogs)
2. Propose the correction to the learner
3. Record the decision and rationale in `learning/decisions.md`
4. Update `learning/curriculum.md` if the change is structural

Do **not** silently perpetuate errors discovered during teaching.

## 12. Key Paths (for quick agent reference)

```
learning/current_stage.md   ← session entry point
learning/curriculum.md      ← full Stage catalog
learning/paper_log.md       ← paper reading tracker
learning/decisions.md       ← architectural decisions
notes/main.tex              ← LaTeX book root
notes/preamble.tex          ← shared LaTeX preamble
notes/references.bib        ← BibTeX database
src/lnn/                    ← pure PyTorch implementations
tests/                      ← pytest suite
reference/timeline.md       ← LNN historical timeline
```

## 13. Development Environment

- The canonical local Python environment is the Conda environment `deep_learning`.
- VS Code must use `/home/van-gogh/miniconda3/envs/deep_learning/bin/python`.
- Install this package editable into that environment with `python -m pip install -e ".[dev]"`.
- Do not create a project-local virtual environment unless the learner explicitly changes this policy.

## 14. Git Stewardship

Hermes is responsible for routine Git maintenance for this repository:

- Keep commits small, coherent, and tied to verified learning or engineering milestones.
- Run the relevant tests, Ruff checks, and LaTeX build before committing changes that affect them.
- Push verified commits to `origin/main` unless a change warrants an isolated feature branch.
- Never rewrite published history, force-push, delete branches, or discard learner changes without explicit approval.
- Never commit credentials, local caches, generated LaTeX auxiliaries, datasets, or large experiment artifacts.
