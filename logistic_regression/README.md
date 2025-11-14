# Logistic Regression

Binary classifier trained with gradient descent on log-loss.

Usage:

```python
from algorithm import fit_logistic_regression, predict

X = [[0.0], [1.0], [2.0]]
y = [0, 0, 1]
w, b = fit_logistic_regression(X, y)
print(predict(w, b, [1.5]))
```