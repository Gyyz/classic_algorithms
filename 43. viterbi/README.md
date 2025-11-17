# Viterbi Algorithm

Dynamic programming method to find the most likely sequence of hidden states (Viterbi path) given observations in a hidden Markov model (HMM).

Key ideas:

- Recurrence on best path probabilities.
- Backpointers to reconstruct the optimal path.

Overview

- Computes MAP sequence of hidden states in HMM given emissions and transitions.

Algorithm Steps

1. Initialize `δ_0(i) = π_i · b_i(o_0)`.
2. Recurrence: `δ_t(j) = max_i [δ_{t-1}(i) · a_{ij}] · b_j(o_t)`; store argmax backpointers.
3. Terminate at `argmax_i δ_T(i)`; backtrack via pointers.

Complexity

- `O(T · S^2)` for `T` timesteps and `S` states.

Usage Example

```python
from algorithm import viterbi
states = viterbi(obs, start_prob, trans_prob, emit_prob)
```