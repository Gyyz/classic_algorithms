# Union-Find (Disjoint Set Union)

Data structure maintaining a partition of elements into disjoint sets, supporting:

- Find: locate the representative of an element’s set.
- Union: merge two sets.

With union by rank and path compression, operations run near-constant time.

Overview

- Maintains disjoint sets with efficient merges and finds; used in Kruskal’s MST, connectivity, and clustering.

Operations

- `find(x)`: returns representative; `union(x,y)`: merges sets.
- Optimizations: path compression flattens trees; union by rank/size controls height.

Complexity

- Amortized inverse Ackermann time `α(n)` per op (effectively constant).

Usage Example

```python
from algorithm import UnionFind
uf = UnionFind(n=10)
uf.union(1,2); uf.union(2,3)
print(uf.find(3))
```