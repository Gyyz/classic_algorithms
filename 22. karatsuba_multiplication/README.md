# Karatsuba Multiplication

An efficient divide-and-conquer algorithm for multiplying large integers faster than the classical grade-school method.

Key ideas:

- Split numbers into high/low parts.
- Three recursive multiplications vs. four.
- Combine with shifts.

Overview

- Reduces multiplication complexity from `O(n^2)` to `O(n^{log_2 3}) ≈ O(n^{1.585})`.
- Splits operands and reuses partial results to cut one multiplication.

Algorithm Steps

1. Split `x = x1·B + x0`, `y = y1·B + y0`.
2. Compute `z0 = x0*y0`, `z2 = x1*y1`, `z1 = (x0+x1)(y0+y1) - z0 - z2`.
3. Combine: `x*y = z2·B^2 + z1·B + z0`.

Complexity

- `T(n) = 3T(n/2) + O(n)` ⇒ `O(n^{log_2 3})`.

Usage Example

```python
from algorithm import karatsuba
print(karatsuba(12345678, 98765432))
```