# K-Means Clustering

Unsupervised clustering with k centroids; assigns points to nearest centroid.

Usage:

```python
from algorithm import KMeans

X = [[0,0],[0,1],[10,10],[10,11]]
km = KMeans(k=2, seed=0).fit(X)
print(km.centroids)
print(km.predict([0.5, 0.5]))
```