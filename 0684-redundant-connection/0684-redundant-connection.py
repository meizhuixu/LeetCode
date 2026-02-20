class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, u):
        if self.parent[u] == u:
            return u
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

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for u, v in edges:
            if uf.isSame(u, v):
                return [u, v]
            uf.join(u, v)

        return
        