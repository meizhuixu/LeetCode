class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # edge case: 1 point
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

        uf = UnionFind(n)
        total_cost = count = 0
        for dist, u, v in edges:
            if uf.join(u, v):
                total_cost += dist
                count += 1
                if count == n - 1:
                    return total_cost

        return total_cost






