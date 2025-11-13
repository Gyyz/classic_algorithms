# Buchberger's Algorithm (Toy)

Buchberger's algorithm transforms generators of a polynomial ideal into a Gröbner basis with respect to a monomial order by repeatedly computing S-polynomials and reducing them.

Key ideas (toy version):

- Represent multivariate polynomials as dicts of monomials to coefficients.
- Use lex order on exponents.
- Iterate S-polynomial and reduction until no new elements appear.

This is an educational, small-scale implementation for 2 variables.