# K-Nearest Neighbors

Overview

- Instance-based classifier: assigns label by majority vote among the `k` closest training points.
- Uses Euclidean distance; no explicit training beyond storing data.

Algorithm

- Compute distances from query point to all training points; take `k` with smallest distance; majority vote.

When To Use

- Simple baseline for small datasets; non-parametric and can capture non-linear decision boundaries.

Complexity

- Prediction O(n · d) per query (`n` samples, `d` dimensions). Training cost is negligible.

Pros and Cons

- Pros: simple, no training, flexible.
- Cons: slow for large `n`; sensitive to feature scaling and choice of `k`.

Usage

```python
from algorithm import KNNClassifier

X = [[0,0],[1,1],[2,2]]
y = ["A","A","B"]
clf = KNNClassifier(k=3).fit(X, y)
print(clf.predict([1.5, 1.5]))
```

Notes

- Standardize features for mixed scales; consider KD-trees/ANN for faster queries.