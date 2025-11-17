# Simplex Algorithm

Popular technique for solving linear programs (LPs) by moving along vertices of the feasible polytope to improve the objective.

Key ideas:

- Standard form with slack variables.
- Pivot operations to reach optimality or detect unboundedness.

Overview

- Moves along vertices of the feasible polytope, improving objective until optimal.
- Variants: Bland’s rule, dual simplex; interior-point methods are alternatives.

Algorithm Steps (Tableau)

1. Convert LP to standard form; add slack variables.
2. Choose entering/leaving variables via pivot rules.
3. Perform pivot; repeat until optimal or unbounded/infeasible.

Complexity

- Worst-case exponential; typically fast in practice on many instances.

Usage Example

```python
from algorithm import simplex
opt, x = simplex(A, b, c)
```