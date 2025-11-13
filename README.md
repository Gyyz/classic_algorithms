# Algorithm Intro Project

A curated collection of classic algorithms and data structures, each in its own self-contained module with a short README and a simple runnable demo.

## Repository Structure
- Each algorithm lives in a dedicated folder, typically containing:
  - `README.md`: concept overview and key ideas.
  - `algorithm.py`: minimal implementation and an `__main__` demo.
- Some modules include `__init__.py` or notebooks in `notebooks/` for interactive exploration.

## Quick Start
- Run any demo directly:
  - `python a_star/algorithm.py`
  - `python maximum_flow/algorithm.py`
  - `python merge_sort/algorithm.py`
  - `python svd/algorithm.py` (requires `numpy`)
- Optional dependencies:
  - `numpy` for `svd/`.
  - `pytest` for running tests (`python -m pytest -q`).

## Algorithms Index

### Graphs and Paths
- [A* Search](a_star/) — best-first pathfinding with heuristics.
- [Dijkstra](dijkstra/) — single-source shortest paths on nonnegative weights.
- [Maximum Flow](maximum_flow/) — Edmonds–Karp (BFS augmenting paths).
- [Beam Search](beam_search/) — pruned best-first heuristic search.
- [Branch and Bound](branch_and_bound/) — systematic search with bounding.

### Sorting and Data Structures
- [Merge Sort](merge_sort/) — stable `O(n log n)` divide-and-conquer sort.
- [Heaps & Heap Sort](heaps_heap_sort/) — heap operations and in-place sort.
- [Binary Search](binary_search/) — logarithmic-time lookup in sorted arrays.
- [Union-Find](union_find/) — disjoint sets with path compression.

### Numerical & Linear Algebra
- [FFT](fft/) — Cooley–Tukey fast Fourier transform and inverse.
- [SVD](svd/) — singular value decomposition via NumPy.
- [Linear Systems](linear_systems/) — Gauss–Jordan solver for `Ax=b`.
- [Gradient Descent](gradient_descent/) — simple 1D optimizer.
- [Newton's Method](newtons_method/) — root finding in one dimension.
- [Discrete Differentiation](discrete_differentiation/) — finite differences.

### Optimization & Probabilistic Methods
- [Simplex](simplex/) — tableau-based LP solver for small problems.
- [Expectation Maximization](expectation_maximization/) — parameter estimation.
- [Viterbi](viterbi/) — HMM most-likely state sequence via DP.
- [RANSAC](ransac/) — robust model fitting with outliers.
- [Edit Distance](dynamic_programming_edit_distance/) — DP string similarity.

### Algebra, Number Theory, and Cryptography
- [Euclidean Algorithm](euclidean_algorithm/) — GCD computation.
- [Karatsuba Multiplication](karatsuba_multiplication/) — fast integer multiply.
- [Hashing](hashing/) and [Polynomial Hashing](hashing_polynomial/) — hashing basics.
- [LLL Algorithm](lll_algorithm/) — lattice basis reduction (overview/demo).
- [Diffie-Hellman](diffie_hellman/) — key exchange.
- [RSA](rsa/) — keygen (Miller–Rabin), encrypt/decrypt demo.
- [Quadratic Sieve](quadratic_sieve/) — stub module with notes.
- [Schönhage–Strassen](schonhage_strassen/) — stub module with notes.
- [Buchberger Algorithm](buchberger_algorithm/) — Gröbner bases basics.

### Signal & Imaging
- [Structure Tensor](strukturtensor/) — edge/corner measures via second moments.

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


To run any demo:

```
python <algorithm_folder>/algorithm.py
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