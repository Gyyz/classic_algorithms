import math
from collections import Counter


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


class KNNClassifier:
    def __init__(self, k=3):
        self.k = k
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = X
        self.y = y
        return self

    def predict(self, x):
        dists = [(distance(x, xi), yi) for xi, yi in zip(self.X, self.y)]
        dists.sort(key=lambda t: t[0])
        neighbors = [c for _, c in dists[: self.k]]
        counts = Counter(neighbors)
        return max(counts, key=lambda k: counts[k])


if __name__ == "__main__":
    X = [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [0.9, 1.1]]
    y = ["A", "A", "B", "A"]
    clf = KNNClassifier(k=3).fit(X, y)
    print(clf.predict([1.5, 1.5]))  