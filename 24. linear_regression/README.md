# Linear Regression

Overview

- Fits a straight line `y ≈ a x + b` to minimize mean squared error (ordinary least squares, OLS).
- This implementation is univariate (one feature `x`) and uses the closed-form normal equations.

Formulation

- Objective: minimize `MSE(a, b) = (1/n) Σ (y_i − (a x_i + b))^2`.
- Closed-form solution: `a = (n Σ x_i y_i − (Σ x_i)(Σ y_i)) / (n Σ x_i^2 − (Σ x_i)^2)`, `b = (Σ y_i − a Σ x_i) / n`.

When To Use

- Fast baseline for continuous targets with roughly linear relation to the feature.
- Interpretable; useful for small datasets and quick diagnostics.

Complexity

- O(n) time and O(1) space for the univariate closed-form computation.

Pros and Cons

- Pros: simple, interpretable, fast.
- Cons: sensitive to outliers; assumes linearity; here only univariate.

Usage

```python
from algorithm import fit_linear_regression, predict

X = [0, 1, 2, 3]
y = [1, 3, 5, 7]
a, b = fit_linear_regression(X, y)
print(a, b)
print(predict(a, b, [10]))
```

Notes

- For multiple features, OLS extends to matrices; this repo includes a minimal univariate version.