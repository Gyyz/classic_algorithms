# Decision Tree (Stump)

Overview

- A decision stump is a one-level decision tree: split on a single threshold over one feature.
- This implementation selects the threshold that maximizes information gain (reduces entropy of labels).

Formulation

- Entropy: `H(Y) = − Σ p(y) log2 p(y)`.
- Information gain for split at threshold `t`: `IG = H(Y) − [ (n_left/n) H(Y_left) + (n_right/n) H(Y_right) ]`.

When To Use

- Interpretable 1D classifier; often used as weak learners in ensembles (boosting/forests).

Complexity

- Sorting O(n log n), scanning candidate thresholds O(n). Overall O(n log n).

Pros and Cons

- Pros: interpretable, captures simple threshold rules.
- Cons: limited expressiveness; prone to overfitting if used alone.

Usage

```python
from algorithm import DecisionStump

X = [0.1, 0.5, 1.0]
y = ["A", "A", "B"]
model = DecisionStump().fit(X, y)
print(model.predict(0.7))
```

Notes

- For multi-feature and deeper trees, extend to recursive splitting with pruning.