# Naive Bayes (Multinomial)

Simple multinomial Naive Bayes for tokenized documents with Laplace smoothing.

Usage:

```python
from algorithm import MultinomialNaiveBayes

docs = [["cat", "cute"], ["dog", "loyal"]]
labels = ["cat", "dog"]
nb = MultinomialNaiveBayes().fit(docs, labels)
print(nb.predict(["cute"]))
```