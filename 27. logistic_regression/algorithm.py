import math


def sigmoid(z):
    # Numerically stable sigmoid
    if z >= 0:
        ez = math.exp(-z)
        return 1 / (1 + ez)
    else:
        ez = math.exp(z)
        return ez / (1 + ez)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def fit_logistic_regression(X, y, lr=0.1, iters=1000):
    # Binary labels in {0,1}; X is list of feature lists
    if not X:
        raise ValueError("Empty dataset")
    d = len(X[0])
    w = [0.0] * d
    b = 0.0
    for _ in range(iters):
        gw = [0.0] * d
        gb = 0.0
        for xi, yi in zip(X, y):
            p = sigmoid(dot(w, xi) + b)
            err = p - yi
            for j in range(d):
                gw[j] += err * xi[j]
            gb += err
        n = len(X)
        for j in range(d):
            w[j] -= lr * gw[j] / n
        b -= lr * gb / n
    return w, b


def predict_proba(w, b, x):
    return sigmoid(dot(w, x) + b)


def predict(w, b, x, threshold=0.5):
    return 1 if predict_proba(w, b, x) >= threshold else 0


if __name__ == "__main__":
    # Simple XOR-like but linearly separable with augmented feature
    X = [[0.0], [1.0], [2.0], [3.0]]
    y = [0, 0, 1, 1]
    w, b = fit_logistic_regression(X, y, lr=0.5, iters=2000)
    print("Logistic regression weights:", w, "bias:", b)
    for x in X:
        print(x, "->", predict_proba(w, b, x), predict(w, b, x))