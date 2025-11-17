# Apriori

Overview

- Mines frequent itemsets from transactional data and derives association rules.
- Uses the anti-monotonic property: if an itemset is frequent, all its subsets are frequent.

Algorithm

- Generate candidate itemsets level by level (size `k` from size `k−1`).
- Prune candidates whose subsets are not frequent; count support across transactions; keep those meeting `min_support`.
- Association rules: for frequent itemset `A∪B`, compute `confidence = support(A∪B)/support(A)`; keep those above `min_confidence`.

When To Use

- Market basket analysis, co-occurrence discovery in logs or events.

Complexity

- Exponential worst-case in number of items; pruning reduces search but large, dense datasets remain costly.

Pros and Cons

- Pros: interpretable rules; simple candidate generation and pruning.
- Cons: can be slow for large item universes; many trivial rules if thresholds are low.

Usage

```python
from algorithm import apriori, generate_rules

transactions = [["milk","bread"],["milk","diaper"],["bread","diaper"]]
fi = apriori(transactions, min_support=0.5)
rules = generate_rules(fi, min_confidence=0.7)
print(fi)
print(rules)
```

Notes

- Tune `min_support` and `min_confidence` to balance rule quantity and relevance; consider FP-Growth for performance.