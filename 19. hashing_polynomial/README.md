# Hashing: Polynomial Rolling Hash

A lightweight string hashing scheme that treats characters as coefficients of a polynomial evaluated at a base, modulo a large number.

Key ideas:

- `hash(s) = Σ s[i]*base^i (mod M)`.
- Supports efficient prefix hashing and substring hashes.