class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.count = 1

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        else:
            self.parent[u] = v
            self.count += 1
            return True

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        total_cost = 0

        for x, y, cost in connections:
            if uf.join(x, y):
                total_cost += cost
            if uf.count == n:
                return total_cost

        return -1


        