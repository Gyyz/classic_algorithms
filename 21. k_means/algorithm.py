import random


def mean(points):
    d = len(points[0])
    return [sum(p[j] for p in points) / len(points) for j in range(d)]


class KMeans:
    def __init__(self, k=3, iters=100, seed=None):
        self.k = k
        self.iters = iters
        self.seed = seed
        self.centroids = None

    def fit(self, X):
        rng = random.Random(self.seed)
        self.centroids = [X[rng.randrange(len(X))] for _ in range(self.k)]
        for _ in range(self.iters):
            clusters = [[] for _ in range(self.k)]
            for x in X:
                idx = min(range(self.k), key=lambda i: sum((x[j] - self.centroids[i][j]) ** 2 for j in range(len(x))))
                clusters[idx].append(x)
            new_centroids = []
            for i in range(self.k):
                if clusters[i]:
                    new_centroids.append(mean(clusters[i]))
                else:
                    new_centroids.append(self.centroids[i])
            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids
        return self

    def predict(self, x):
        return min(range(self.k), key=lambda i: sum((x[j] - self.centroids[i][j]) ** 2 for j in range(len(x))))


if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [10, 10], [10, 11], [11, 10]]
    km = KMeans(k=2, seed=42).fit(X)
    print("Centroids:", km.centroids)
    print("Cluster of [0.5,0.5]:", km.predict([0.5, 0.5]))