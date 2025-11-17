# Discrete Differentiation (Central Difference)

Approximate the derivative using the central difference formula:

`f'(x) ≈ (f(x+h) - f(x-h)) / (2h)`.

Key ideas:

- Symmetric finite difference reduces error.
- Choose small `h` but not too small to avoid floating-point issues.

Overview

- Finite difference approximations: forward, backward, central; central has higher accuracy for smooth functions.

Error and Stability

- Truncation error scales with `h^2` for central difference; round-off grows when `h` is too small.
- Pick `h` balancing truncation and floating-point error (e.g., `sqrt(eps)` scale).

Usage Example

```python
from algorithm import central_diff
df = central_diff(f, x, h=1e-3)
```