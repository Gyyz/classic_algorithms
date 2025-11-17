# Solving Linear Systems

Systems of linear equations appear throughout science and engineering. Efficient solvers include Gauss–Jordan elimination and Cholesky decomposition.

This module demonstrates Gauss–Jordan elimination for small dense systems.

Overview

- Solve `Ax = b` via elimination; pivoting improves numerical stability.
- Alternatives: LU/Cholesky factorization, iterative solvers for large sparse systems.

Algorithm Steps (Gauss–Jordan)

1. Augment `[A|b]` and perform row operations to reach reduced row echelon form.
2. Read off solution from the transformed system.

Complexity

- Dense elimination `O(n^3)`; memory `O(n^2)`.

Usage Example

```python
from algorithm import gauss_jordan
x = gauss_jordan([[2,1],[5,7]], [11,13])
```

Notes

- Use pivoting to avoid division by tiny numbers.