# Hashing (General)

Hashing maps data to fixed-size digests. This general intro references a simple polynomial rolling hash implementation in `hashing_polynomial`.

Overview

- Deterministic mapping from inputs to fixed-size outputs; collisions possible.
- Used for hash tables, checksums, cryptographic digests (with additional properties).

Types

- Non-cryptographic (e.g., polynomial rolling, MurmurHash): fast, good distribution.
- Cryptographic (e.g., SHA-256): collision/second-preimage resistance.

Complexity

- Typically linear in input size; constant-time lookup with good hash tables.

Usage Example

```python
from hashing_polynomial.algorithm import poly_hash
h = poly_hash("hello", base=257, mod=2**61-1)
```