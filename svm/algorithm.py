def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def add(u, v):
    return [a + b for a, b in zip(u, v)]


def sub(u, v):
    return [a - b for a, b in zip(u, v)]


def scale(u, s):
    return [a * s for a in u]


class LinearSVM:
    # Hinge loss, gradient descent; labels in {-1, +1}
    def __init__(self, lr=0.1, iters=1000, C=1.0):
        self.lr = lr
        self.iters = iters
        self.C = C
        self.w = None
        self.b = 0.0

    def fit(self, X, y):
        d = len(X[0])
        self.w = [0.0] * d
        self.b = 0.0
        for _ in range(self.iters):
            gw = [0.0] * d
            gb = 0.0
            for xi, yi in zip(X, y):
                margin = yi * (dot(self.w, xi) + self.b)
                if margin < 1:
                    gw = add(gw, scale(xi, -self.C * yi))
                    gb += -self.C * yi
            self.w = sub(self.w, scale(gw, self.lr / len(X)))
            self.b -= self.lr * gb / len(X)
        return self

    def decision_function(self, x):
        return dot(self.w, x) + self.b

    def predict(self, x):
        return 1 if self.decision_function(x) >= 0 else -1


if __name__ == "__main__":
    X = [[0.0], [1.0], [2.0], [3.0]]
    y = [-1, -1, 1, 1]
    svm = LinearSVM(lr=0.5, iters=2000, C=1.0).fit(X, y)
    for x in X:
        print(x, "->", svm.predict(x))