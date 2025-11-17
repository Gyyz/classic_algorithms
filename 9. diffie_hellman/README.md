# Diffie–Hellman Key Exchange

Diffie–Hellman allows two parties to agree on a shared secret over an insecure channel using modular exponentiation with a large prime `p` and generator `g`.

Key ideas:

- Each party picks a private exponent.
- Exchanges `g^a mod p` and `g^b mod p`.
- Both compute `(g^b)^a ≡ (g^a)^b ≡ g^{ab} (mod p)`.

This demo uses small numbers for clarity.