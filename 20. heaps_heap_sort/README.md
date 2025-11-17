# Heaps and Heap Sort

A heap is a tree-based data structure supporting efficient insertion and extraction of the minimum/maximum. Heap sort uses a heap to sort in `O(n log n)` time.

Key ideas:

- Heap property: parent ≥ children (max-heap) or ≤ (min-heap).
- Heapify and repeated extract to sort.

Overview

- Binary heap supports `insert`, `extract-max/min`, `peek` in `O(log n)`.
- Heap sort: build heap `O(n)` then extract repeatedly `O(n log n)`.

Algorithm Steps (Heap Sort)

1. Heapify array.
2. For `i=n..1`: swap max with end, reduce heap size, sift-down.

Complexity

- Time `O(n log n)`; space `O(1)` in-place (max-heap version).

Usage Example

```python
from algorithm import heap_sort
print(heap_sort([5,1,4,2,8]))
```

Notes

- Unstable sort; for stability, use merge sort.