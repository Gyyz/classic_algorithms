# Gradient Boosting (1D)

Overview

- Ensemble method that builds a strong regressor by sequentially fitting weak learners to residuals.
- This implementation uses 1D decision stumps as weak learners.

Algorithm

- Initialize model with a constant (mean of targets).
- For each iteration: fit a stump to current residuals (target − model prediction), and add it to the model scaled by `learning_rate`.
- Final prediction is the sum of the initial value and all scaled stump outputs.

When To Use

- Powerful for tabular data; captures non-linear patterns with appropriate weak learners.

Complexity

- Training O(T · n log n) roughly (stump fitting cost) where `T` is number of estimators; inference O(T).

Pros and Cons

- Pros: strong performance, handles complex patterns, controllable bias/variance via `learning_rate` and `n_estimators`.
- Cons: can overfit without regularization; sensitive to learning rate; here limited to 1D stumps.

Usage

```python
from algorithm import GradientBoostingRegressor1D

X = [0,1,2,3]
y = [0,1,4,9]
gbr = GradientBoostingRegressor1D(n_estimators=20, learning_rate=0.1).fit(X, y)
print(gbr.predict(2.5))
```

Notes

- Extend to multi-feature weak learners (trees) for stronger models; add shrinkage and subsampling to regularize.