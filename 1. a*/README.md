# A* Search

A* is a best-first graph search algorithm that finds a path from a start node to a goal node using a heuristic estimate `h(n)` of the remaining cost. It prioritizes nodes with minimal `f(n) = g(n) + h(n)`, where `g(n)` is the path cost from the start.

Key ideas:

- Uses a priority queue ordered by `f(n)`.
- Admissible heuristics (never overestimate) ensure optimality.
- Common heuristic on grids: Manhattan distance.

This demo uses a 2D grid, 4-neighbor moves, and Manhattan heuristic.