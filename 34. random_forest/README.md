# Random Forest (Stumps)

Overview

- Ensemble of weak learners (decision stumps) trained on bootstrapped samples; prediction by majority vote.
- Reduces variance and mitigates overfitting compared to a single stump.

Algorithm

- For each estimator: sample with replacement a subset of training data (bagging), fit a stump.
- Prediction: collect votes from all stumps for the input; choose the most frequent class.

When To Use

- Stronger than a single threshold rule; useful baseline for 1D feature problems.

Complexity

- Training O(T · n log n) where `T` is number of stumps; inference O(T).

Pros and Cons

- Pros: robust, reduces variance, simple.
- Cons: with stumps only, limited decision boundaries; for richer patterns use deeper trees.

Usage

```python
from algorithm import RandomForestStumps

X = [0.1, 0.5, 1.0, 1.5]
y = ["A", "A", "B", "B"]
rf = RandomForestStumps(n_estimators=15).fit(X, y)
print(rf.predict(0.7))
```

Notes

- In classic random forests, each node considers a random subset of features; here features are 1D.