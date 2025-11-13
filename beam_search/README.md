# Beam Search

Beam search is a heuristic search that limits the number of nodes considered at each depth to a fixed beam width `m`. It keeps only the `m` most promising candidates according to a scoring function.

Key ideas:

- Like best-first search, but prunes aggressively.
- Trades optimality for speed and memory.
- Commonly used in decoding sequences (e.g., NLP).

This demo searches paths in a simple graph using a heuristic score.