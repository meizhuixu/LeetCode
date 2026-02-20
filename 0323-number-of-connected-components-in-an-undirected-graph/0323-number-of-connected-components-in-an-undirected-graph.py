class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

    def isSame(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.parent[u] = v
        self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.join(u, v)

        return uf.count
        