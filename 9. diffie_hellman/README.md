# Diffie–Hellman Key Exchange

Diffie–Hellman allows two parties to agree on a shared secret over an insecure channel using modular exponentiation with a large prime `p` and generator `g`.

Key ideas:

- Each party picks a private exponent.
- Exchanges `g^a mod p` and `g^b mod p`.
- Both compute `(g^b)^a ≡ (g^a)^b ≡ g^{ab} (mod p)`.

This demo uses small numbers for clarity.

Overview

- Establishes a shared secret via exponentiation modulo a large prime; relies on hardness of discrete log.
- Basis for many protocols; in practice uses large safe primes and standardized groups.

Protocol Steps

1. Agree on prime `p` and generator `g` of a cyclic group.
2. Alice picks secret `a`, sends `A = g^a mod p`; Bob picks `b`, sends `B = g^b mod p`.
3. Alice computes `s = B^a mod p`; Bob computes `s = A^b mod p`; shared secret `s`.

Security

- Eavesdropper sees `g`, `p`, `A`, `B`; computing `s` requires solving discrete log.
- Use ephemeral keys and authentication to prevent MITM.

Usage Example

```python
from algorithm import diffie_hellman_demo
shared = diffie_hellman_demo(p, g)
```