# Expectation–Maximization (EM)

EM alternates between estimating latent variables (E-step) and maximizing parameters (M-step) to find maximum likelihood estimates.

This demo fits a 1D two-component Gaussian mixture.

Key ideas:

- E-step: responsibilities via current parameters.
- M-step: update means, variances, and mixture weights.

Overview

- Iterative ML estimation with latent variables; monotone increase in likelihood.
- Applied to mixture models, missing data, HMMs (Baum–Welch).

Algorithm Steps (GMM)

1. Initialize parameters (means, variances, weights).
2. E-step: compute responsibilities `r_{ik}` given current params.
3. M-step: update parameters using responsibilities.

Complexity

- Per iteration: `O(nk)` for `k` components; converges to local optimum.

Usage Example

```python
from algorithm import em_gaussian_mixture
params = em_gaussian_mixture(X, k=2, max_iters=50)
```

Notes

- Initialization matters; use multiple restarts to avoid poor local optima.