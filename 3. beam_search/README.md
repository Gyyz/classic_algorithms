# Beam Search

Beam search is a heuristic search that limits the number of nodes considered at each depth to a fixed beam width `m`. It keeps only the `m` most promising candidates according to a scoring function.

Key ideas:

- Like best-first search, but prunes aggressively.
- Trades optimality for speed and memory.
- Commonly used in decoding sequences (e.g., NLP).

This demo searches paths in a simple graph using a heuristic score.

Overview

- Keeps top `m` candidates at each depth according to a scoring function.
- Approximates best-first search with reduced memory and faster runtime.

Algorithm Steps

1. Start with initial beam of candidates.
2. Expand all candidates to next-step children.
3. Score children; keep top `m` as new beam.
4. Repeat until stopping criterion (goal found, max depth).

Complexity

- Per depth, work is `O(m * b)` where `b` is branching factor; overall depends on depth.
- Memory capped by `m` and representation size.

Pros / Cons

- Pros: controllable runtime/memory; good for sequence decoding.
- Cons: not optimal; can prune away optimal paths.

Usage Example

```python
from algorithm import beam_search
path = beam_search(start, is_goal, expand_fn, score_fn, beam_width=5)
print(path)
```

Notes

- Tune `beam_width` to balance quality and speed.
- Use problem-specific scoring (e.g., language model likelihood in NLP).