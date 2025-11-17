# Logistic Regression

Overview

- Binary classification model that maps inputs to probability of class 1 via the sigmoid function.
- Trained by minimizing logistic (cross-entropy) loss using gradient descent.

Formulation

- Model: `p(y=1|x) = σ(w·x + b)` with `σ(z) = 1/(1+e^{-z})`.
- Loss: `L = (1/n) Σ [− y_i log p_i − (1−y_i) log(1−p_i)]`.
- Prediction: threshold probability at 0.5 by default.

When To Use

- Binary classification with linearly separable decision boundary or as a strong baseline.

Complexity

- Per iteration O(n·d) where `n` is samples and `d` features; number of iterations depends on convergence.

Pros and Cons

- Pros: calibrated probabilities, robust baseline, simple to implement.
- Cons: linear boundary; performance degrades for complex non-linear patterns.

Usage

```python
from algorithm import fit_logistic_regression, predict

X = [[0.0], [1.0], [2.0]]
y = [0, 0, 1]
w, b = fit_logistic_regression(X, y)
print(predict(w, b, [1.5]))
```

Notes

- Regularization is not included here; for noisy data add L2/L1 penalties to improve generalization.