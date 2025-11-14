import random
from collections import Counter


class DecisionStump:
    def __init__(self):
        self.threshold = None
        self.left_label = None
        self.right_label = None

    def fit(self, X, y):
        pairs = sorted(zip(X, y), key=lambda t: t[0])
        xs = [p[0] for p in pairs]
        ys = [p[1] for p in pairs]
        best_t = None
        best_left = None
        best_right = None
        best_score = -float('inf')
        # Simple majority vote gain
        from collections import Counter as C
        base = max(C(ys).values())
        for i in range(1, len(xs)):
            if xs[i] == xs[i - 1]:
                continue
            t = (xs[i] + xs[i - 1]) / 2
            left = ys[:i]
            right = ys[i:]
            score = max(C(left).values()) + max(C(right).values())
            if score > best_score:
                best_score = score
                best_t = t
                best_left = max(C(left), key=lambda k: C(left)[k])
                best_right = max(C(right), key=lambda k: C(right)[k])
        self.threshold = best_t
        self.left_label = best_left
        self.right_label = best_right
        return self

    def predict(self, x):
        return self.left_label if x < self.threshold else self.right_label


class RandomForestStumps:
    def __init__(self, n_estimators=10, sample_ratio=0.7, seed=None):
        self.n_estimators = n_estimators
        self.sample_ratio = sample_ratio
        self.models = []
        self.seed = seed

    def fit(self, X, y):
        rng = random.Random(self.seed)
        n = len(X)
        self.models = []
        for _ in range(self.n_estimators):
            k = max(1, int(self.sample_ratio * n))
            idxs = [rng.randrange(n) for _ in range(k)]
            Xi = [X[i] for i in idxs]
            yi = [y[i] for i in idxs]
            model = DecisionStump().fit(Xi, yi)
            self.models.append(model)
        return self

    def predict(self, x):
        votes = [m.predict(x) for m in self.models]
        c = Counter(votes)
        return max(c, key=lambda k: c[k])


if __name__ == "__main__":
    X = [0.1, 0.5, 1.0, 1.5, 2.0]
    y = ["A", "A", "B", "B", "B"]
    rf = RandomForestStumps(n_estimators=25, seed=42).fit(X, y)
    for v in X:
        print(v, "->", rf.predict(v))