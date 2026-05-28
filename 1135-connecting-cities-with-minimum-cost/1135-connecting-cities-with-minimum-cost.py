class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))   # let 0 be empty

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
            return True


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x:x[2])
        total_cost, left_connections = 0, n - 1
        uf = UnionFind(n)

        for u, v, cost in connections:
            if uf.join(u, v): # return True
                total_cost += cost
                left_connections -= 1
            if left_connections == 0:
                return total_cost

        return -1




        