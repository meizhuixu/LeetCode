class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # edge case: 1 point

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, dist))

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        pq = [(0, 0)]
        visited = [False] * n
        total_cost = connected = 0
        while pq:
            cost, point = heapq.heappop(pq)

            if visited[point]:
                continue

            visited[point] = True
            total_cost += cost
            connected += 1
            if connected == n:
                return total_cost

            for dc, nxt in graph[point]:
                if not visited[nxt]:
                    heapq.heappush(pq, (dc, nxt))

        return