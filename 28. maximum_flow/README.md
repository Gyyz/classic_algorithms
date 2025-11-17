# Maximum Flow (Ford–Fulkerson / Edmonds–Karp)

The maximum flow problem seeks a legal flow through a directed network that maximizes the total flow from a source to a sink. By the max-flow min-cut theorem, the value of the maximum flow equals the capacity of the minimum cut.

Key ideas:

- Maintain a residual network capturing remaining capacities.
- Repeatedly find augmenting paths and push flow until none remain.
- Edmonds–Karp uses BFS for shortest augmenting paths, ensuring `O(V * E^2)` complexity.

Overview

- Network flow on directed graphs with capacities and conservation constraints.
- Applications: bipartite matching, circulation, image segmentation.

Algorithm Steps (Edmonds–Karp)

1. Build residual graph; while there is an `s→t` path, push flow.
2. Path via BFS (shortest edge count); update residual capacities.
3. Terminate when no augmenting path exists.

Complexity

- `O(V E^2)` for Edmonds–Karp; Dinic’s improves to `O(E V^2)`.

Usage Example

```python
from algorithm import max_flow
value, flow = max_flow(graph, s, t)
```