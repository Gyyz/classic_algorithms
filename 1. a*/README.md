# A* Search

A* is a best-first graph search algorithm that finds a path from a start node to a goal node using a heuristic estimate `h(n)` of the remaining cost. It prioritizes nodes with minimal `f(n) = g(n) + h(n)`, where `g(n)` is the path cost from the start.

Key ideas:

- Uses a priority queue ordered by `f(n)`.
- Admissible heuristics (never overestimate) ensure optimality.
- Common heuristic on grids: Manhattan distance.

This demo uses a 2D grid, 4-neighbor moves, and Manhattan heuristic.

Overview

- Expands nodes by lowest `f = g + h`. Optimal if `h` is admissible and consistent.
- Suitable for pathfinding on grids, road networks, and graphs with known heuristics.

Algorithm Steps

1. Initialize open set with start; set `g(start)=0`.
2. Pop node with lowest `f`; if goal, reconstruct path via parents.
3. For each neighbor, compute tentative `g`; if lower, update parent and `f`.
4. Repeat until goal or open set empty.

Complexity

- Worst-case time `O(E log V)` with a binary heap; practical speed depends on heuristic quality.
- Memory `O(V)` for open/closed sets and parent map.

Pros / Cons

- Pros: often faster than Dijkstra; optimal with good heuristic.
- Cons: memory-intensive; needs domain-informed heuristic.

Usage Example

```python
from algorithm import astar

path, cost = astar(start, goal, neighbors_fn, cost_fn, heuristic_fn)
print(path)
```

Notes

- Use consistent heuristics to guarantee optimality and avoid re-open logic.
- If `h = 0`, A* degenerates to Dijkstra.