class DecisionStumpRegressor:
    # 1D decision stump for regression: predicts left/right means
    def __init__(self):
        self.threshold = None
        self.left_value = 0.0
        self.right_value = 0.0

    def fit(self, X, y):
        pairs = sorted(zip(X, y), key=lambda t: t[0])
        xs = [p[0] for p in pairs]
        ys = [p[1] for p in pairs]
        best_loss = float('inf')
        best_t = None
        best_left = 0.0
        best_right = 0.0
        for i in range(1, len(xs)):
            if xs[i] == xs[i - 1]:
                continue
            t = (xs[i] + xs[i - 1]) / 2
            left = ys[:i]
            right = ys[i:]
            if not left or not right:
                continue
            ml = sum(left) / len(left)
            mr = sum(right) / len(right)
            loss = sum((v - ml) ** 2 for v in left) + sum((v - mr) ** 2 for v in right)
            if loss < best_loss:
                best_loss = loss
                best_t = t
                best_left = ml
                best_right = mr
        self.threshold = best_t
        self.left_value = best_left
        self.right_value = best_right
        return self

    def predict(self, x):
        return self.left_value if x < self.threshold else self.right_value


class GradientBoostingRegressor1D:
    def __init__(self, n_estimators=50, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models = []
        self.init_value = 0.0

    def fit(self, X, y):
        self.init_value = sum(y) / len(y)
        residuals = [yi - self.init_value for yi in y]
        self.models = []
        for _ in range(self.n_estimators):
            stump = DecisionStumpRegressor().fit(X, residuals)
            self.models.append(stump)
            # Update residuals
            residuals = [ri - self.learning_rate * stump.predict(xi) for ri, xi in zip(residuals, X)]
        return self

    def predict(self, x):
        val = self.init_value
        for m in self.models:
            val += self.learning_rate * m.predict(x)
        return val


if __name__ == "__main__":
    # Sample noisy quadratic
    X = [0, 1, 2, 3, 4, 5]
    y = [0.0, 1.1, 4.2, 9.1, 16.4, 26.0]
    gbr = GradientBoostingRegressor1D(n_estimators=30, learning_rate=0.2).fit(X, y)
    for x in X:
        print(x, "->", gbr.predict(x))