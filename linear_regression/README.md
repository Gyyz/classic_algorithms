# Linear Regression

Univariate ordinary least squares. Fits `y ≈ a x + b` via closed-form normal equations.

Usage:

```python
from algorithm import fit_linear_regression, predict

X = [0, 1, 2, 3]
y = [1, 3, 5, 7]
a, b = fit_linear_regression(X, y)
print(a, b)
print(predict(a, b, [10]))
```