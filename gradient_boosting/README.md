# Gradient Boosting (1D)

Simple gradient boosting regressor using decision stumps over a single feature.

Usage:

```python
from algorithm import GradientBoostingRegressor1D

X = [0,1,2,3]
y = [0,1,4,9]
gbr = GradientBoostingRegressor1D(n_estimators=20, learning_rate=0.1).fit(X, y)
print(gbr.predict(2.5))
```