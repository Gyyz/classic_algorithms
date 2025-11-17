# Singular Value Decomposition (SVD)

Factorization of a matrix `A` into `U Σ V^T`, with applications to pseudoinverses, least squares, dimensionality reduction, and more.

Note:

- This demo uses NumPy if available.
- For full numerical robustness, rely on established libraries.

Overview

- Factor `A = U Σ V^T` with singular values in `Σ`; enables pseudoinverse `A^+`, rank detection, and PCA.

Applications

- Least squares: `x = A^+ b`.
- PCA: use right singular vectors of centered data; singular values relate to variance.

Complexity

- Dense SVD `O(mn·min(m,n))`; use library routines for stability.

Usage Example

```python
from algorithm import svd_demo
U, S, Vt = svd_demo(A)
```