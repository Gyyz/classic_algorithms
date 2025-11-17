# Newton's Method

Efficient iterative algorithm for approximating roots of real-valued functions. Starting from an initial guess, it repeatedly applies `x_{k+1} = x_k - f(x_k)/f'(x_k)` until convergence.

Key ideas:

- Quadratic convergence near simple roots.
- Requires derivative information.
- Extendable to optimization and multivariate settings.