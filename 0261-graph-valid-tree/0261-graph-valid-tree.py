class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.edges = 0

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.parent[u] = v
            self.edges += 1

    def isSame(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: 
        #1. no circle   
        #2. all nodes connected
        # nodes = n, edges = n - 1

        # union find:
        # 1. check if there is a circle: return False
        # 2. check if all nodes are connected
        uf = UnionFind(n)
        for u, v in edges:
            if uf.isSame(u, v):
                return False
            uf.join(u, v)

        return uf.edges == n - 1