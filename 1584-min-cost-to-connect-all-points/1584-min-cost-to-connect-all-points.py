class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        pq = []
        heapq.heappush(pq, (0, 0))
        visited = set()
        res = 0
        while pq:
            d, cur = heapq.heappop(pq)
            if cur in visited:
                continue
            visited.add(cur)
            res += d

            for nxt_d, nxt in graph[cur]:
                if nxt not in visited:
                    heapq.heappush(pq, (nxt_d, nxt))

        return res


