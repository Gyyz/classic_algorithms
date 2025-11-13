# Dijkstra's Algorithm

Dijkstra solves the single-source shortest path problem on graphs with nonnegative edge weights using a greedy strategy with a priority queue.

Key ideas:

- Maintain tentative distances.
- Extract minimum distance node and relax neighbors.
- Complexity: `O((V+E) log V)` with a heap.