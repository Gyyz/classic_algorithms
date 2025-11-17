class DisjointSet:
    def __init__(self, elements=None):
        self.parent = {}
        self.rank = {}
        if elements:
            for e in elements:
                self.make_set(e)

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        px = self.parent.get(x, x)
        if px != x:
            self.parent[x] = self.find(px)
        return self.parent.get(x, x)

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class UnionFind(DisjointSet):
    """
    Alias class to match README usage. Inherits DisjointSet functionality.
    """
    pass

if __name__ == "__main__":
    ds = DisjointSet(range(5))
    ds.union(0, 1)
    ds.union(3, 4)
    print("connected(0,1):", ds.connected(0,1))
    print("connected(1,2):", ds.connected(1,2))