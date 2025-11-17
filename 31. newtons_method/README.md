# Newton's Method

Efficient iterative algorithm for approximating roots of real-valued functions. Starting from an initial guess, it repeatedly applies `x_{k+1} = x_k - f(x_k)/f'(x_k)` until convergence.

Key ideas:

- Quadratic convergence near simple roots.
- Requires derivative information.
- Extendable to optimization and multivariate settings.

Overview

- Root-finding via tangent line approximation; converges rapidly near solution if `f'` nonzero.

Algorithm Steps

1. Pick initial guess `x0`.
2. Iterate `x_{k+1} = x_k - f(x_k)/f'(x_k)` until convergence.

Complexity

- Per iteration: cost of evaluating `f` and `f'`; quadratic convergence near simple roots.

Usage Example

```python
from algorithm import newton
root = newton(lambda x: x**2-2, lambda x: 2*x, x0=1.0)
```

Notes

- Divergence possible if `f'` near zero or poor initial guess; use safeguards.