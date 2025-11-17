# RSA

Public-key cryptosystem suitable for encryption and signatures. Security relies on the difficulty of factoring large integers. Keys must be sufficiently large for security.

Key ideas:

- Choose primes p, q; compute n = p q and φ(n) = (p-1)(q-1).
- Pick e coprime to φ(n); compute d as modular inverse of e mod φ(n).
- Encrypt: c ≡ m^e (mod n); Decrypt: m ≡ c^d (mod n).

Overview

- Public-key cryptosystem based on integer factorization; used for encryption and signatures.

Key Generation

1. Choose large primes `p`, `q`; compute `n=pq` and `φ=(p-1)(q-1)`.
2. Pick public exponent `e` (e.g., 65537) coprime to `φ`; compute private `d ≡ e^{-1} (mod φ)`.

Encryption/Decryption

- Encrypt: `c ≡ m^e (mod n)`; Decrypt: `m ≡ c^d (mod n)`.
- Use padding (e.g., OAEP) for semantic security.

Security Notes

- Avoid small primes, use random generation and primality tests.
- Use CRT for faster decryption; protect against side-channel attacks.

Usage Example

```python
from algorithm import rsa_keygen, rsa_encrypt, rsa_decrypt
(n, e, d) = rsa_keygen(bits=1024)
c = rsa_encrypt(n, e, 12345)
m = rsa_decrypt(n, d, c)
```