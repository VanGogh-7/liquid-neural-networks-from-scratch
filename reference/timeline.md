# LNN Historical Timeline

Calibrated against original paper publication dates. Curriculum Stage order is pedagogical, not strictly chronological.

```
──────┬─────────────────────────────────────────────────────────────────────
 1993 │ Funahashi & Nakamura — Continuous-time RNN approximation theory
      │ (CT-RNNs as universal approximators of dynamical systems)
──────┼─────────────────────────────────────────────────────────────────────
 2018 │ Chen et al. — Neural Ordinary Differential Equations (NeurIPS)
      │ Differentiable ODE solvers; adjoint method; continuous-depth models
──────┼─────────────────────────────────────────────────────────────────────
 2020 │ Lechner, Hasani et al. — Neural Circuit Policies (Nature MI)
      │ C. elegans-inspired sparse wiring; sensory→inter→command→motor
──────┼─────────────────────────────────────────────────────────────────────
2020/ │ Hasani, Lechner, Amini, Rus, Grosu — Liquid Time-Constant Networks
 2021 │ (AAAI 2021, arXiv June 2020)
      │ Input/state-dependent time constants; electrical circuit foundation
──────┼─────────────────────────────────────────────────────────────────────
 2022 │ Hasani, Lechner, Amini et al. — Closed-form Continuous-time Networks
      │ (Nature Machine Intelligence)
      │ Analytical approximation eliminating ODE solver overhead
──────┼─────────────────────────────────────────────────────────────────────
 2022 │ Hasani, Lechner et al. — Liquid Structural State-Space Models
      │ (arXiv:2209.12951)
      │ LTC-informed S4; state-of-the-art on Long Range Arena (87.32%)
──────┼─────────────────────────────────────────────────────────────────────
 2024 │ Farsang et al. — Saturated Liquid Time-Constant Networks (STC)
      │ Sigmoid/tanh gating on conductances
──────┼─────────────────────────────────────────────────────────────────────
 2024 │ Farsang et al. — Liquid Resistance Liquid Capacitance Networks (LRC)
      │ (arXiv:2403.08791)
      │ State-dependent capacitance; LRCU as efficient gated unit
──────┼─────────────────────────────────────────────────────────────────────
 2025 │ Farsang, Hasani, Rus, Grosu — LrcSSM (NeurIPS 2025)
      │ Diagonal Jacobian → parallel prefix scan; O(TD) time, O(log T) depth
──────┼─────────────────────────────────────────────────────────────────────
2025+ │ Active frontiers: Liquid-GNN, Liquid-CNN, neuromorphic deployment,
      │ dual liquid dynamics, scalable pretraining, interpretability
──────┴─────────────────────────────────────────────────────────────────────
```

## Relationship Between Curriculum Order and Chronology

Curriculum order follows pedagogical dependency, not strict chronology:

- Part I (Stages 00–03): Mathematical foundations — ahistorical (tools, not discoveries)
- Part II (Stages 04–05): CT-RNN (1993 concept) → Neural ODE (2018) — correct chronological order
- Part III (Stages 06–09): NCP (2020) → LTC (2020/2021) → LTC theory — correct order
- Part IV (Stages 10–11): CfC (2022) — follows LTC, correct
- Part V (Stages 12–14): SSM theory → S4 (2022) → Liquid-S4 (2022) — SSM theory predates S4 conceptually but the curriculum teaches it as a prerequisite
- Part VI (Stages 15–19): STC (2024) → LRC (2024) → LRCU (2024) → LrcSSM (2025) → Frontiers — correct chronological order
