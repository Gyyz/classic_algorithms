# Q-learning

Q-learning is a model-free reinforcement learning method that learns an action-value function `Q(s, a)`, estimating the expected utility of taking action `a` in state `s` and following a policy thereafter.

Key ideas:

- Temporal-difference updates: `Q <- Q + α (r + γ max_a' Q(s', a') - Q)`.
- Off-policy; does not require a model of the environment.
- Uses exploration strategies (e.g., ε-greedy).

Overview

- Model-free RL; learns `Q` via experience; optimal policy `π(s) = argmax_a Q(s,a)`.

Algorithm Steps

1. Initialize `Q(s,a)` arbitrarily.
2. At each step, choose action (ε-greedy), observe reward `r` and next state `s'`.
3. Update: `Q(s,a) ← Q(s,a) + α [r + γ max_{a'} Q(s',a') - Q(s,a)]`.

Complexity

- Depends on state/action space size and exploration; converges under standard assumptions.

Usage Example

```python
from algorithm import q_learning
Q = q_learning(env, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1)
```

Notes

- Use decaying ε and learning rate; consider Double Q-learning to reduce overestimation.