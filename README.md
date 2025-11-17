# Algorithm Intro Project

A curated collection of classic algorithms and data structures, each in its own self-contained module with a short README and a simple runnable demo.

## Repository Structure
- Each algorithm lives in a dedicated folder, typically containing:
  - `README.md`: concept overview and key ideas.
  - `algorithm.py`: minimal implementation and an `__main__` demo.
- Some modules include `__init__.py` or notebooks in `notebooks/` for interactive exploration.

## Quick Start
- Run any demo directly:
  - `python "1. a*/algorithm.py"`
  - `python "28. maximum_flow/algorithm.py"`
  - `python "29. merge_sort/algorithm.py"`
  - `python "40. svd/algorithm.py"` (requires `numpy`)
- Optional dependencies:
  - `numpy` for `40. svd/`.
  - `pytest` for running tests (`python -m pytest -q`).

## Algorithms Index

### Graphs and Paths
- [A* Search](1. a*/) — best-first pathfinding with heuristics.
- [Dijkstra](10. dijkstra/) — single-source shortest paths on nonnegative weights.
- [Maximum Flow](28. maximum_flow/) — Edmonds–Karp (BFS augmenting paths).
- [Beam Search](3. beam_search/) — pruned best-first heuristic search.
- [Branch and Bound](5. branch_and_bound/) — systematic search with bounding.

### Sorting and Data Structures
- [Merge Sort](29. merge_sort/) — stable `O(n log n)` divide-and-conquer sort.
- [Heaps & Heap Sort](20. heaps_heap_sort/) — heap operations and in-place sort.
- [Binary Search](4. binary_search/) — logarithmic-time lookup in sorted arrays.
- [Union-Find](42. union_find/) — disjoint sets with path compression.

### Numerical & Linear Algebra
- [FFT](15. fft/) — Cooley–Tukey fast Fourier transform and inverse.
- [SVD](40. svd/) — singular value decomposition via NumPy.
- [Linear Systems](25. linear_systems/) — Gauss–Jordan solver for `Ax=b`.
- [Gradient Descent](17. gradient_descent/) — simple 1D optimizer.
- [Newton's Method](31. newtons_method/) — root finding in one dimension.
- [Discrete Differentiation](11. discrete_differentiation/) — finite differences.

### Optimization & Probabilistic Methods
- [Simplex](38. simplex/) — tableau-based LP solver for small problems.
- [Expectation Maximization](14. expectation_maximization/) — parameter estimation.
- [Viterbi](43. viterbi/) — HMM most-likely state sequence via DP.
- [RANSAC](35. ransac/) — robust model fitting with outliers.
- [Edit Distance](12. dynamic_programming_edit_distance/) — DP string similarity.

### Algebra, Number Theory, and Cryptography
- [Euclidean Algorithm](13. euclidean_algorithm/) — GCD computation.
- [Karatsuba Multiplication](22. karatsuba_multiplication/) — fast integer multiply.
- [Hashing](18. hashing/) and [Polynomial Hashing](19. hashing_polynomial/) — hashing basics.
- [LLL Algorithm](26. lll_algorithm/) — lattice basis reduction (overview/demo).
- [Diffie-Hellman](9. diffie_hellman/) — key exchange.
- [RSA](36. rsa/) — keygen (Miller–Rabin), encrypt/decrypt demo.
- [Quadratic Sieve](33. quadratic_sieve/) — stub module with notes.
- [Schönhage–Strassen](37. schonhage_strassen/) — stub module with notes.
- [Buchberger Algorithm](6. buchberger_algorithm/) — Gröbner bases basics.

### Signal & Imaging
- [Structure Tensor](39. strukturtensor/) — edge/corner measures via second moments.

## Notebooks
- Interactive demos in `notebooks/` (e.g., `a_star.ipynb`, `fft.ipynb`, `gradient_descent.ipynb`). Open with Jupyter or VS Code.

## Testing
- Existing tests: `tests/test_fft.py`, `tests/test_heap_sort.py`, `tests/test_edit_distance.py`.
- Run all tests: `python -m pytest -q`.

## Contributing
- Keep modules small and focused, with a clear `README.md`.
- Provide a tiny `__main__` example in `algorithm.py`.
- Prefer readable code and minimal dependencies.

This repository provides a brief introduction and a minimal Python implementation for several widely used algorithms in computer science and mathematics. Each algorithm has its own folder containing:

- `README.md`: A concise overview and key ideas.
- `algorithm.py`: A minimal, runnable Python demonstration.

Algorithms included:

- A* search
- Beam search
- Binary search
- Branch and bound (0/1 knapsack)
- Buchberger's algorithm (toy Gröbner basis)
- Huffman data compression (encode/decode)
- Diffie–Hellman key exchange (demonstration)
- Dijkstra's shortest path
- Discrete differentiation (central difference)
- Dynamic programming (edit distance)
- Euclidean algorithm (GCD)
- Expectation–Maximization (1D Gaussian Mixture)
- Fast Fourier Transform (Cooley–Tukey)
- Gradient descent (quadratic function)
- Hashing (polynomial rolling hash)
- Heaps (heap sort)
- Karatsuba multiplication
- LLL lattice reduction (basic educational version)
- Linear systems (Gauss-Jordan elimination)
- Maximum flow (Edmonds–Karp)
- Merge sort
- Newton's method (1D root finding)
- Quadratic sieve (toy implementation)
- RANSAC (robust model fitting)
- RSA (keygen, encrypt/decrypt)
- Schönhage–Strassen (toy implementation)
- Singular value decomposition (SVD)
- Simplex (LP solver)
- Structure tensor (edge/corner detection)
- Union-find (disjoint sets)
- Viterbi (HMM state sequence)


To run any demo (paths contain spaces, wrap in quotes):

```
python "<number>. <folder>/algorithm.py"
```

Tests

- Quick tests are provided for edit distance, FFT round-trip, and heap sort.
- Run with:

```
python tests/test_edit_distance.py
python tests/test_fft.py
python tests/test_heap_sort.py
```

Jupyter Notebooks

- Interactive notebooks with simple plots live in `notebooks/`.
- Recommended tools: `pip install jupyter matplotlib numpy ipywidgets`.
- Launch with:

```
jupyter notebook notebooks/
```

Interactive notebooks:

- `a_star_interactive.ipynb`: step-by-step A* with obstacle probability and step slider.
- `dijkstra_relaxation.ipynb`: visualizes relaxation steps and distance changes.
- `fft_interactive.ipynb`: mix two sinusoids and explore spectrum via sliders.
- `gradient_descent_interactive.ipynb`: tune learning rate and steps to see convergence.