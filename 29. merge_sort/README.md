# Merge Sort

A divide-and-conquer sorting algorithm that recursively splits a list into halves, sorts each half, and merges the sorted halves to produce an ordered list.

Key ideas:

- Recursively sort halves.
- Linear-time merge step.
- Stable and runs in `O(n log n)`.

Overview

- Divide-and-conquer with stable merge; good for linked lists and external sorting.

Algorithm Steps

1. If `n<=1`, return.
2. Split into halves; recursively sort each.
3. Merge two sorted lists in linear time.

Complexity

- Time `O(n log n)`; space `O(n)` (arrays) or `O(1)` (linked lists with pointer manipulation).

Usage Example

```python
from algorithm import merge_sort
print(merge_sort([5,2,4,6,1,3]))
```