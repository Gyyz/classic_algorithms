# Dijkstra's Algorithm

Dijkstra solves the single-source shortest path problem on graphs with nonnegative edge weights using a greedy strategy with a priority queue.

Key ideas:

- Maintain tentative distances.
- Extract minimum distance node and relax neighbors.
- Complexity: `O((V+E) log V)` with a heap.

Overview

- Greedy algorithm for shortest paths in graphs with nonnegative edge weights.
- Uses a priority queue to pick the next closest node and relax edges.

Algorithm Steps

1. Initialize distances `dist[s]=0`, others `∞`; push `(0,s)`.
2. Pop node `u`; for each neighbor `v`, relax: if `dist[u]+w(u,v) < dist[v]`, update and push.
3. Continue until queue empty.

Complexity

- `O((V+E) log V)` using a binary heap; `O(V^2)` with arrays.

Usage Example

```python
from algorithm import dijkstra
dist = dijkstra(graph, source)
```

Notes

- For negative edges, use Bellman–Ford; for undirected trees, BFS suffices.