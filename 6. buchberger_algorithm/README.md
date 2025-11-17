# Buchberger's Algorithm (Toy)

Buchberger's algorithm transforms generators of a polynomial ideal into a Gröbner basis with respect to a monomial order by repeatedly computing S-polynomials and reducing them.

Key ideas (toy version):

- Represent multivariate polynomials as dicts of monomials to coefficients.
- Use lex order on exponents.
- Iterate S-polynomial and reduction until no new elements appear.

This is an educational, small-scale implementation for 2 variables.

Overview

- Computes a Gröbner basis for an ideal given generators under a chosen monomial order.
- Key operations: S-polynomial computation and polynomial reduction.

Algorithm Steps (Toy)

1. Start with set `G` of generators.
2. For each pair `(f,g) ∈ G`, compute S-polynomial `S(f,g)`.
3. Reduce `S` modulo `G`; if nonzero, add to `G`.
4. Repeat until no additions; `G` is a Gröbner basis.

Complexity

- Can be expensive; depends on degrees and variable count; practical implementations use criteria (Buchberger's) to skip pairs.

Pros / Cons

- Pros: enables ideal membership tests, solving polynomial systems via elimination.
- Cons: computationally heavy; sensitive to monomial order.

Usage Example

```python
from algorithm import grobner_basis
G = grobner_basis([f, g], order="lex")
```