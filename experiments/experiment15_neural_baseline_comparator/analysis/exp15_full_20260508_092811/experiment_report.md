# Experiment 15 Analysis Report

Generated: 2026-05-08T14:22:42.373985+00:00
Run ID: `exp15_full_20260508_092811`
Profile: `full`

## Purpose

Experiment 15 compares small neural sequence baselines against transition, seen-route, suffix-route, context-conflict, retention, and runtime probes.

## Hardest-slice metric summary

Hardest summarized slice: `world_count=32`, `route_length=12`.

| variant                                   | metric_name                          |        mean |        ci95 |   n_seeds |
|:------------------------------------------|:-------------------------------------|------------:|------------:|----------:|
| neural_gru_endpoint_context               | first_step_context_conflict_accuracy | 0           | 0           |        10 |
| neural_gru_endpoint_context               | retention_after_sequential_worlds    | 0.701497    | 0.0171981   |        10 |
| neural_gru_endpoint_context               | seen_route_composition_accuracy      | 0.998958    | 0.00155935  |        10 |
| neural_gru_endpoint_context               | suffix_route_composition_accuracy    | 0.404036    | 0.0340121   |        10 |
| neural_gru_endpoint_context               | transition_accuracy                  | 0.0231554   | 0.0012426   |        10 |
| neural_gru_endpoint_no_context            | first_step_context_conflict_accuracy | 0           | 0           |        10 |
| neural_gru_endpoint_no_context            | retention_after_sequential_worlds    | 0.0230859   | 0.000615858 |        10 |
| neural_gru_endpoint_no_context            | seen_route_composition_accuracy      | 0.03125     | 0           |        10 |
| neural_gru_endpoint_no_context            | suffix_route_composition_accuracy    | 0.0149219   | 0.00123172  |        10 |
| neural_gru_endpoint_no_context            | transition_accuracy                  | 0.000911458 | 0.00029605  |        10 |
| neural_gru_rollout_context                | first_step_context_conflict_accuracy | 0.879427    | 0.0141951   |        10 |
| neural_gru_rollout_context                | retention_after_sequential_worlds    | 0.061237    | 0.0067041   |        10 |
| neural_gru_rollout_context                | seen_route_composition_accuracy      | 0.0447917   | 0.00675432  |        10 |
| neural_gru_rollout_context                | suffix_route_composition_accuracy    | 0.0776823   | 0.00876473  |        10 |
| neural_gru_rollout_context                | transition_accuracy                  | 0.512174    | 0.0194725   |        10 |
| neural_gru_rollout_no_context             | first_step_context_conflict_accuracy | 0.03125     | 0           |        10 |
| neural_gru_rollout_no_context             | retention_after_sequential_worlds    | 0.0222396   | 0.00485266  |        10 |
| neural_gru_rollout_no_context             | seen_route_composition_accuracy      | 0.00078125  | 0.000779674 |        10 |
| neural_gru_rollout_no_context             | suffix_route_composition_accuracy    | 0.0436979   | 0.009365    |        10 |
| neural_gru_rollout_no_context             | transition_accuracy                  | 0.435004    | 0.0376804   |        10 |
| neural_transformer_sequence_context       | first_step_context_conflict_accuracy | 0           | 0           |        10 |
| neural_transformer_sequence_context       | retention_after_sequential_worlds    | 0.330937    | 0.0313687   |        10 |
| neural_transformer_sequence_context       | seen_route_composition_accuracy      | 0.54349     | 0.0586871   |        10 |
| neural_transformer_sequence_context       | suffix_route_composition_accuracy    | 0.118385    | 0.0109481   |        10 |
| neural_transformer_sequence_context       | transition_accuracy                  | 0.00696615  | 0.000726972 |        10 |
| neural_transition_mlp_context             | first_step_context_conflict_accuracy | 1           | 0           |        10 |
| neural_transition_mlp_context             | retention_after_sequential_worlds    | 1           | 0           |        10 |
| neural_transition_mlp_context             | seen_route_composition_accuracy      | 1           | 0           |        10 |
| neural_transition_mlp_context             | suffix_route_composition_accuracy    | 1           | 0           |        10 |
| neural_transition_mlp_context             | transition_accuracy                  | 1           | 0           |        10 |
| neural_transition_mlp_no_context          | first_step_context_conflict_accuracy | 0.03125     | 0           |        10 |
| neural_transition_mlp_no_context          | retention_after_sequential_worlds    | 0.515625    | 0           |        10 |
| neural_transition_mlp_no_context          | seen_route_composition_accuracy      | 0.03125     | 0           |        10 |
| neural_transition_mlp_no_context          | suffix_route_composition_accuracy    | 1           | 0           |        10 |
| neural_transition_mlp_no_context          | transition_accuracy                  | 0.919271    | 0           |        10 |
| neural_transition_mlp_replay_context      | first_step_context_conflict_accuracy | 0.00859375  | 0.00443994  |        10 |
| neural_transition_mlp_replay_context      | retention_after_sequential_worlds    | 0.000481771 | 0.000860884 |        10 |
| neural_transition_mlp_replay_context      | seen_route_composition_accuracy      | 0.000520833 | 0.00102083  |        10 |
| neural_transition_mlp_replay_context      | suffix_route_composition_accuracy    | 0.000442708 | 0.00070582  |        10 |
| neural_transition_mlp_replay_context      | transition_accuracy                  | 0.0119792   | 0.00367804  |        10 |
| neural_transition_mlp_world_heads_context | first_step_context_conflict_accuracy | 1           | 0           |        10 |
| neural_transition_mlp_world_heads_context | retention_after_sequential_worlds    | 1           | 0           |        10 |
| neural_transition_mlp_world_heads_context | seen_route_composition_accuracy      | 1           | 0           |        10 |
| neural_transition_mlp_world_heads_context | suffix_route_composition_accuracy    | 1           | 0           |        10 |
| neural_transition_mlp_world_heads_context | transition_accuracy                  | 1           | 0           |        10 |

## Runtime summary

| variant                                   |   runtime_seconds |
|:------------------------------------------|------------------:|
| neural_transition_mlp_world_heads_context |          67.4711  |
| neural_transition_mlp_replay_context      |          15.7324  |
| neural_transition_mlp_no_context          |          10.6503  |
| neural_transition_mlp_context             |          10.3868  |
| neural_gru_rollout_no_context             |           9.46143 |
| neural_gru_rollout_context                |           9.44742 |
| neural_transformer_sequence_context       |           8.36522 |
| neural_gru_endpoint_context               |           5.5151  |
| neural_gru_endpoint_no_context            |           5.38649 |

## Interpretation guardrails

- Do not treat Exp15 as an exhaustive architecture search.
- Endpoint models and transition/rollout models answer different questions.
- No-context failures are meaningful because the generator creates incompatible world-specific successors.
- Replay and parameter isolation are conventional neural controls, not biological claims.
