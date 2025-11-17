# Euclidean Algorithm (GCD)

Computes the greatest common divisor (GCD) of two integers using repeated remainder reductions.

Key ideas:

- `gcd(a, b) = gcd(b, a mod b)`.
- Terminates when remainder is 0.

Overview

- Classic algorithm for GCD using modular reduction; extended version finds Bezout coefficients.

Algorithm Steps

1. While `b != 0`: `(a, b) = (b, a % b)`.
2. Return `a`.

Complexity

- Time `O(log min(a,b))` with division steps.

Usage Example

```python
from algorithm import gcd
print(gcd(48, 18))  # 6
```

Notes

- Extended Euclidean yields `x,y` such that `ax + by = gcd(a,b)`.