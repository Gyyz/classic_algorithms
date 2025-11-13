# Binary Search

Binary search locates a target in a sorted array by repeatedly halving the search interval. It runs in `O(log n)` time.

Key ideas:

- Maintain low/high indices.
- Compare mid value to target.
- Update bounds until found or interval empty.