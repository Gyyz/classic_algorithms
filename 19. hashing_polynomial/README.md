# Hashing: Polynomial Rolling Hash

A lightweight string hashing scheme that treats characters as coefficients of a polynomial evaluated at a base, modulo a large number.

Key ideas:

- `hash(s) = Σ s[i]*base^i (mod M)`.
- Supports efficient prefix hashing and substring hashes.

Overview

- With modular arithmetic and base selection, achieves good dispersion and fast operations.
- Common in string algorithms (pattern matching, rolling hashes).

Complexity

- `O(n)` to compute hash; `O(1)` substring hash with precomputed powers and prefix hashes.

Usage Example

```python
from algorithm import poly_hash, build_prefix
h, pref, powb = build_prefix(s, base=257, mod=2**61-1)
# substring [l..r)
sub = (pref[r] - pref[l] * powb[r-l]) % mod
```

Notes

- Choose large modulus (e.g., 64-bit prime) and base to reduce collisions.