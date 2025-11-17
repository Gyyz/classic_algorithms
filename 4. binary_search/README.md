# Binary Search

Binary search locates a target in a sorted array by repeatedly halving the search interval. It runs in `O(log n)` time.

Key ideas:

- Maintain low/high indices.
- Compare mid value to target.
- Update bounds until found or interval empty.

Overview

- Searches sorted arrays by halving the interval based on comparisons.
- Requires monotonic order and random access.

Algorithm Steps

1. Set `lo=0`, `hi=n-1`.
2. While `lo<=hi`: `mid=(lo+hi)//2`, compare `arr[mid]` to target.
3. Move `lo` or `hi` based on comparison; return index if found.

Complexity

- Time `O(log n)`; space `O(1)` iterative.

Variants

- Lower/upper bound, first/last occurrence, insert position.

Usage Example

```python
from algorithm import binary_search
idx = binary_search([1,3,4,7,9], 7)
print(idx)  # 3
```

Notes

- Beware integer overflow in some languages when computing `mid`.
- For floats/monotone predicates, use binary search on condition domain.