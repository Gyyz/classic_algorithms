# Support Vector Machine (Linear)

Overview

- Maximum-margin classifier that finds a linear decision boundary with largest margin between classes.
- This implementation uses soft-margin hinge loss optimized via gradient descent.

Formulation

- Decision function: `f(x) = w·x + b`; predict `sign(f(x))`.
- Hinge loss with regularization: `L = (1/n) Σ max(0, 1 − y_i f(x_i)) + C · R(w)` where `y ∈ {−1,+1}` and `R(w)` is weight penalty (implicit here).
- Gradient updates penalize margin violations (points inside the margin or misclassified).

When To Use

- Strong baseline for high-dimensional data; works well with small datasets and clear linear separability.

Complexity

- Per iteration O(n·d); convergence depends on learning rate and data separability.

Pros and Cons

- Pros: robust margins, effective in high dimensions, interpretable linear boundary.
- Cons: linear only; kernel methods needed for non-linear structures (not included here).

Usage

```python
from algorithm import LinearSVM

X = [[0.0],[1.0],[2.0],[3.0]]
y = [-1,-1,1,1]
svm = LinearSVM().fit(X, y)
print(svm.predict([1.5]))
```

Notes

- Tune `C` to trade off margin size vs. violations; add explicit L2 regularization for stability.