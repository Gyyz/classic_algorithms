# LLL Algorithm (Basic Educational Version)

The Lenstra–Lenstra–Lovász (LLL) algorithm reduces a lattice basis to one with shorter, nearly orthogonal vectors.

Key ideas:

- Gram–Schmidt orthogonalization to compute projections.
- Size reduction and Lovász condition.
- Iteratively swap and reduce until stable.

This demo handles small integer bases.

Overview

- Reduces lattice basis to nearly orthogonal vectors; useful in factoring, cryptanalysis, and Diophantine approximation.

Algorithm Steps

1. Gram–Schmidt to get orthogonal components.
2. Size reduction to keep coefficients small.
3. Lovász condition; swap and repeat until stable.

Complexity

- Polynomial-time in dimension and input size; practical performance good for small dimensions.

Usage Example

```python
from algorithm import lll_reduce
B_red = lll_reduce(B)
```