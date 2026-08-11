# Learning Handoffs

This directory contains the authoritative bridge between external learning and repository work.

## File naming

Use one file per Stage when a handoff is ready:

```text
stage_00.md
stage_01.md
...
stage_19.md
```

Copy `TEMPLATE.md` and complete every section. Use `N/A` with a short reason when a field does not apply; do not silently omit fields.

## Authority and acceptance

- The learner or the learning interface prepares the handoff after completing the applicable learning lifecycle.
- `Learning status: LEARNED` asserts that the learning outcomes have been checked outside Hermes.
- Hermes reviews the handoff against `learning/curriculum.md`, the repository notation policy, and the Stage exit criteria.
- Receipt of a handoff changes `Repository Status` to `HANDOFF`; it does not automatically mean the handoff is accepted.
- During `INTEGRATE`, Hermes identifies missing evidence, unsupported conclusions, notation conflicts, source gaps, and required repository artifacts.
- Major mathematical conclusions must come from the handoff or verified sources. Incomplete chat snippets must not override a complete handoff.
- Corrections made during integration remain visible in the handoff or are recorded in `learning/decisions.md`; do not silently alter learner-derived conclusions.

## Evidence categories

When integrating LaTeX or implementation requirements, distinguish:

1. **Learner-derived** — explanations or derivations completed and understood by the learner.
2. **Textbook fact** — standard mathematical or engineering material verified independently.
3. **Paper-specific claim** — a claim, notation choice, theorem, method, or result attributable to a cited source.

Paper-specific claims require a primary-source citation whenever possible.
