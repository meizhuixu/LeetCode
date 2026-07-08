class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    # def isSame(self, u, v):
    #     u = self.find(u)
    #     v = self.find(v)
    #     return u == v

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        self.parent[u] = v
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edges = n - 1
        if len(edges) != n - 1:
            return False

        # no cycle
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.join(u, v):
                return False

        return True
