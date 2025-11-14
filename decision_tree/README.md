# Decision Tree (Stump)

Simple 1D threshold-based classifier using information gain.

Usage:

```python
from algorithm import DecisionStump

X = [0.1, 0.5, 1.0]
y = ["A", "A", "B"]
model = DecisionStump().fit(X, y)
print(model.predict(0.7))
```