# Apriori

Frequent itemset mining and association rule generation from transactional data.

Usage:

```python
from algorithm import apriori, generate_rules

transactions = [["milk","bread"],["milk","diaper"],["bread","diaper"]]
fi = apriori(transactions, min_support=0.5)
rules = generate_rules(fi, min_confidence=0.7)
print(fi)
print(rules)
```