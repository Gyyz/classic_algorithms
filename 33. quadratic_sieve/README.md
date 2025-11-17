# Quadratic Sieve (QS)

The quadratic sieve is a modern integer factorization algorithm, second fastest in practice after the number field sieve, and typically best for integers under ~110 digits.

Note:

- A full implementation is complex and lengthy.
- This module provides a stub and references for further development.

Overview

- Factorization via finding congruences of squares modulo `n` using a factor base and smooth numbers.

High-Level Steps

1. Choose factor base of small primes.
2. Find `x` such that `x^2 mod n` is B-smooth over the base.
3. Set up linear system over GF(2) on exponents; find dependency to produce squares.
4. Compute `g = gcd(x - y, n)` to get a factor.

Complexity

- Sub-exponential; faster than trial division and Pollard’s Rho for large `n`.

Notes

- Full implementation is substantial; see references on sieving strategies and filtering.