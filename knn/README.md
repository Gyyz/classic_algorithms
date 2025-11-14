# K-Nearest Neighbors

Simple KNN classifier with Euclidean distance on vector features.

Usage:

```python
from algorithm import KNNClassifier

X = [[0,0],[1,1],[2,2]]
y = ["A","A","B"]
clf = KNNClassifier(k=3).fit(X, y)
print(clf.predict([1.5, 1.5]))
```