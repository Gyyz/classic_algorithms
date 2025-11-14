import math
from collections import defaultdict


class MultinomialNaiveBayes:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.class_counts = defaultdict(int)
        self.token_counts = defaultdict(lambda: defaultdict(int))
        self.class_token_totals = defaultdict(int)
        self.vocab = set()
        self.classes = set()

    def fit(self, documents, labels):
        for doc, c in zip(documents, labels):
            self.classes.add(c)
            self.class_counts[c] += 1
            for token in doc:
                self.vocab.add(token)
                self.token_counts[c][token] += 1
                self.class_token_totals[c] += 1
        return self

    def _log_prob_token_given_class(self, token, c):
        V = len(self.vocab)
        num = self.token_counts[c][token] + self.alpha
        den = self.class_token_totals[c] + self.alpha * V
        return math.log(num / den)

    def _log_prior(self, c):
        total = sum(self.class_counts.values())
        return math.log(self.class_counts[c] / total)

    def predict(self, doc):
        best_c = None
        best_score = -float('inf')
        for c in self.classes:
            score = self._log_prior(c)
            for token in doc:
                score += self._log_prob_token_given_class(token, c)
            if score > best_score:
                best_score = score
                best_c = c
        return best_c


if __name__ == "__main__":
    docs = [
        ["cat", "cute", "furry"],
        ["dog", "cute", "loyal"],
        ["cat", "sleep"],
        ["dog", "bark"],
    ]
    labels = ["cat", "dog", "cat", "dog"]
    nb = MultinomialNaiveBayes(alpha=1.0).fit(docs, labels)
    print(nb.predict(["cat", "cute"]))
    print(nb.predict(["loyal", "bark"]))