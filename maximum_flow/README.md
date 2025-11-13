# Maximum Flow (Ford–Fulkerson / Edmonds–Karp)

The maximum flow problem seeks a legal flow through a directed network that maximizes the total flow from a source to a sink. By the max-flow min-cut theorem, the value of the maximum flow equals the capacity of the minimum cut.

Key ideas:

- Maintain a residual network capturing remaining capacities.
- Repeatedly find augmenting paths and push flow until none remain.
- Edmonds–Karp uses BFS for shortest augmenting paths, ensuring `O(V * E^2)` complexity.