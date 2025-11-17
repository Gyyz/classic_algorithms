# K-Means Clustering

Overview

- Partitions data into `k` clusters by minimizing within-cluster squared distances.
- Alternates between assigning points to nearest centroids and recomputing centroids as means.

Algorithm

- Initialize `k` centroids (random points from data here).
- Repeat until convergence or max iterations:
  - Assignment: for each point, pick the cluster with the nearest centroid (Euclidean distance).
  - Update: set each centroid to the mean of points assigned to its cluster.

When To Use

- Exploratory clustering for roughly spherical, similarly sized clusters; fast baseline for segmentation.

Complexity

- Per iteration O(n·k·d) for `n` points, `k` clusters, `d` dimensions.

Pros and Cons

- Pros: simple, fast, scalable.
- Cons: requires choosing `k`; sensitive to initialization; struggles with non-spherical clusters and outliers.

Usage

```python
from algorithm import KMeans

X = [[0,0],[0,1],[10,10],[10,11]]
km = KMeans(k=2, seed=0).fit(X)
print(km.centroids)
print(km.predict([0.5, 0.5]))
```

Notes

- Improve robustness with multiple random initializations or k-means++ seeding; standardize features.