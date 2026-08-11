# Architectural Decisions

Significant design choices and their rationale.

---

## Decision 001 — Repository Bootstrap (2026-08-11)

**Decision**: Created repository skeleton with the full 6-part, 20-stage curriculum as specified.
**Rationale**: The curriculum structure captures the historical evolution and logical dependency chain of LNN research.
**Impact**: All future learning proceeds Stage-by-Stage; LaTeX book and code modules mirror this structure.

## Decision 002 — English-Only Policy for Durable Content

**Decision**: All durable repository content (README, curriculum, learning state, LaTeX, code comments, experiment docs, AGENTS.md) is written in English.
**Rationale**: English is the lingua franca of ML research; all primary papers are in English; ensures consistency and sharability.
**Impact**: Every persistent file uses English.

## Decision 003 — Harness Not Used for Repository Management

**Decision**: The `verified-agent-harness` / `project-lifecycle-harness` is not used for this repository's day-to-day Stage management.
**Rationale**: The curriculum state machine defined in `AGENTS.md` is sufficient. Harness would add complexity without benefit for a learning repository.
**Impact**: Track Stage progress through `learning/current_stage.md` and the markdown log files; use `AGENTS.md` for agent behavior.

## Decision 004 — Flat `src/lnn/` Package Layout

**Decision**: Each architecture family gets its own subpackage directly under `src/lnn/` rather than grouping by Part.
**Rationale**: Simplifies imports (`from lnn.ltc import LTCCell`); allows independent module development across Parts.
**Impact**: 11 subpackages under `src/lnn/`; no nesting by Part.

## Decision 005 — Experiments Directory Organized by Task Type

**Decision**: `experiments/` is organized by task type (foundations, dynamics, timeseries, irregular, long_range) rather than by Stage.
**Rationale**: Some experiments span multiple Stages; a task-oriented layout encourages cross-model comparison.
**Impact**: Experiments reference models from any Stage; no 1:1 mapping between experiments/ and Stages.

## Decision 006 — Canonical VS Code and Python Environment

**Decision**: VS Code uses the local Conda `deep_learning` environment at `/home/van-gogh/miniconda3/envs/deep_learning/bin/python`.
**Rationale**: This environment already provides the project's CUDA-enabled PyTorch installation and avoids duplicating heavyweight dependencies.
**Impact**: Workspace settings, tasks, debugging, tests, and editable installs target this interpreter. No project-local virtual environment is created.

## Decision 007 — Git Stewardship

**Decision**: Hermes manages routine Git operations and GitHub synchronization for this repository.
**Rationale**: Centralized stewardship keeps commits aligned with verified learning milestones and the Stage state machine.
**Impact**: Hermes may commit and push verified work, while destructive Git operations still require explicit learner approval.

## Decision 008 — Stage-Aware Learning Phases

**Decision**: Every Stage explicitly declares applicable lifecycle phases and gives a reason for each `N/A` phase.
**Rationale**: A fixed lifecycle is useful for implementation Stages but creates meaningless work in notation, theory, and survey Stages if applied mechanically.
**Impact**: Applicable phases remain mandatory and ordered; changing a phase profile requires a recorded curriculum decision.

## Decision 009 — Canonical Mathematical and Numerical Conventions

**Decision**: Use column-vector mathematics, output-row/input-column Jacobians, batch-first tensors, time-first ODE callables, explicit paper-notation translation, and task-dependent float64/float32 precision.
**Rationale**: These conventions prevent silent orientation, signature, and precision mismatches across derivations, PyTorch code, and source papers.
**Impact**: New notes, implementations, and tests must follow the conventions in `AGENTS.md` or document a justified interface exception.

## Decision 010 — Development-Friendly Book Pagination

**Decision**: Build the evolving textbook with the `book` class options `oneside,openany`.
**Rationale**: The default two-sided `openright` layout inserted blank pages between stub chapters and Parts, inflating the bootstrap PDF without adding content.
**Impact**: Chapters may start on either page during development; publication layout can be reconsidered when the manuscript is mature.
