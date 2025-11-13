# Q-learning

Q-learning is a model-free reinforcement learning method that learns an action-value function `Q(s, a)`, estimating the expected utility of taking action `a` in state `s` and following a policy thereafter.

Key ideas:

- Temporal-difference updates: `Q <- Q + α (r + γ max_a' Q(s', a') - Q)`.
- Off-policy; does not require a model of the environment.
- Uses exploration strategies (e.g., ε-greedy).