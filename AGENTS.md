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

## 3. Session Recovery

At the start of every new session, if context is limited, read (in order):

1. `AGENTS.md` (this file)
2. `learning/current_stage.md`
3. The relevant Stage section in `learning/curriculum.md`
4. Any necessary code or LaTeX files for the current Stage

Do **not** rely on chat history to recover course state — the learning directory is the source of truth.

## 4. Mathematical Notation Convention

This repository uses a unified notation defined in Stage 00. Core conventions:

| Symbol            | Meaning                  | Typical Shape       |
| ----------------- | ------------------------ | ------------------- |
| $t$               | continuous time          | scalar              |
| $\Delta t$        | time step                | scalar              |
| $\mathbf{x}(t)$   | state vector             | $(d_x,)$            |
| $\mathbf{u}(t)$   | input vector             | $(d_u,)$            |
| $\mathbf{h}(t)$   | hidden state             | $(d_h,)$            |
| $\mathbf{y}(t)$   | output                   | $(d_y,)$            |
| $\mathbf{W}$      | weight matrix            | $(d_{out}, d_{in})$ |
| $\boldsymbol{\theta}$ | parameters           | —                   |
| $\tau$            | time constant            | scalar or per-neuron|
| $\dot{\mathbf{x}}$| time derivative          | same as $\mathbf{x}$|
| $\odot$           | element-wise product     | —                   |

Always annotate shapes on first use in a formula, e.g. $\mathbf{x}(t) \in \mathbb{R}^{d_x}$.

When writing code, bridge notation to tensor shapes explicitly in comments:

```python
# x: (batch, d_x)  —  state vector x(t)
```

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

The agent must not skip stages without an explicit learner request. Even then, note the skip in `learning/decisions.md`.

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
