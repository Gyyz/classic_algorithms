# Expectation–Maximization (EM)

EM alternates between estimating latent variables (E-step) and maximizing parameters (M-step) to find maximum likelihood estimates.

This demo fits a 1D two-component Gaussian mixture.

Key ideas:

- E-step: responsibilities via current parameters.
- M-step: update means, variances, and mixture weights.