# Branch and Bound (0/1 Knapsack)

Branch and bound is a framework for exploring solution spaces while using bounds to prune suboptimal branches. This demo solves 0/1 knapsack.

Key ideas:

- Branch: include or exclude an item.
- Bound: optimistic upper bound to prune.
- Track best feasible solution found so far.

Overview

- Systematically explores decision tree; uses bounds to skip exploring hopeless branches.
- Common in combinatorial optimization (knapsack, TSP variants).

Algorithm Steps (0/1 Knapsack)

1. Sort items by value/weight ratio (for bound).
2. DFS/BFS over include/exclude decisions; compute current weight/value.
3. Upper bound = current value + greedy fill of remaining capacity.
4. Prune if upper bound ≤ best; update best on feasible solutions.

Complexity

- Worst-case exponential; pruning improves practical performance.

Pros / Cons

- Pros: can find optimal solutions with heavy pruning.
- Cons: problem-dependent bounds; may still be slow on large instances.

Usage Example

```python
from algorithm import branch_and_bound_knapsack
best_value, picked = branch_and_bound_knapsack(weights, values, capacity)
```