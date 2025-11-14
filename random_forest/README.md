# Random Forest (Stumps)

Ensemble of decision stumps trained on bootstrapped samples; prediction by majority vote.

Usage:

```python
from algorithm import RandomForestStumps

X = [0.1, 0.5, 1.0, 1.5]
y = ["A", "A", "B", "B"]
rf = RandomForestStumps(n_estimators=15).fit(X, y)
print(rf.predict(0.7))
```