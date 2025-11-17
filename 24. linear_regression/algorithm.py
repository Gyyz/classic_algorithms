def fit_linear_regression(X, y):
    n = len(X)
    if n == 0:
        raise ValueError("Empty dataset")
    sx = sum(X)
    sy = sum(y)
    sxx = sum(x*x for x in X)
    sxy = sum(x*t for x, t in zip(X, y))
    denom = n * sxx - sx * sx
    if denom == 0:
        raise ValueError("Cannot fit: degenerate X distribution")
    a = (n * sxy - sx * sy) / denom
    b = (sy - a * sx) / n
    return a, b


def predict(a, b, X):
    return [a * x + b for x in X]


if __name__ == "__main__":
    # Simple demo: y ≈ 2x + 1 with noise
    X = [0, 1, 2, 3, 4, 5]
    y = [1.1, 2.9, 5.2, 7.1, 8.9, 10.2]
    a, b = fit_linear_regression(X, y)
    preds = predict(a, b, X)
    print("Linear regression fit: a=", a, "b=", b)
    print("Predictions:", preds)