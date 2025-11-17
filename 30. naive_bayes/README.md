# Naive Bayes (Multinomial)

Overview

- Probabilistic classifier for discrete features (tokens) assuming conditional independence of features given the class.
- This implementation uses Laplace smoothing to handle unseen tokens.

Formulation

- Prior: `P(c) = count(c)/n`.
- Likelihood: `P(token|c) ≈ (count(token,c)+α)/(Σ_t count(t,c)+α·|V|)`.
- Score: predict class maximizing `log P(c) + Σ log P(token|c)` over tokens in a document.

When To Use

- Text classification and bag-of-words features; very fast baseline.

Complexity

- Training O(total tokens); inference O(document length×classes).

Pros and Cons

- Pros: simple, fast, works well with high-dimensional sparse data.
- Cons: independence assumption often violated; probabilities can be overconfident.

Usage

```python
from algorithm import MultinomialNaiveBayes

docs = [["cat", "cute"], ["dog", "loyal"]]
labels = ["cat", "dog"]
nb = MultinomialNaiveBayes().fit(docs, labels)
print(nb.predict(["cute"]))
```

Notes

- For continuous features, use Gaussian Naive Bayes; for counts, multinomial is appropriate.