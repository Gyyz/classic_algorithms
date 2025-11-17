# RSA

Public-key cryptosystem suitable for encryption and signatures. Security relies on the difficulty of factoring large integers. Keys must be sufficiently large for security.

Key ideas:

- Choose primes p, q; compute n = p q and φ(n) = (p-1)(q-1).
- Pick e coprime to φ(n); compute d as modular inverse of e mod φ(n).
- Encrypt: c ≡ m^e (mod n); Decrypt: m ≡ c^d (mod n).