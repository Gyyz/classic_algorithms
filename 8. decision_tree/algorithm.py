import math


def entropy(labels):
    total = len(labels)
    if total == 0:
        return 0.0
    from collections import Counter
    counts = Counter(labels)
    ent = 0.0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent


class DecisionStump:
    # Simple 1D threshold-based classifier
    def __init__(self):
        self.threshold = None
        self.left_label = None
        self.right_label = None

    def fit(self, X, y):
        # X: list of floats; y: list of labels
        pairs = sorted(zip(X, y), key=lambda t: t[0])
        xs = [p[0] for p in pairs]
        ys = [p[1] for p in pairs]
        best_gain = -float('inf')
        best_t = None
        best_left = None
        best_right = None
        base_ent = entropy(ys)
        for i in range(1, len(xs)):
            if xs[i] == xs[i - 1]:
                continue
            t = (xs[i] + xs[i - 1]) / 2
            left = ys[:i]
            right = ys[i:]
            gain = base_ent - (len(left) / len(ys)) * entropy(left) - (len(right) / len(ys)) * entropy(right)
            if gain > best_gain:
                best_gain = gain
                best_t = t
                from collections import Counter
                best_left = max(Counter(left), key=lambda k: Counter(left)[k])
                best_right = max(Counter(right), key=lambda k: Counter(right)[k])
        self.threshold = best_t
        self.left_label = best_left
        self.right_label = best_right
        return self

    def predict(self, x):
        if self.threshold is None:
            raise ValueError("Model not fitted")
        return self.left_label if x < self.threshold else self.right_label


if __name__ == "__main__":
    X = [0.1, 0.5, 1.0, 1.5, 2.0]
    y = ["A", "A", "B", "B", "B"]
    stump = DecisionStump().fit(X, y)
    for v in X:
        print(v, "->", stump.predict(v))