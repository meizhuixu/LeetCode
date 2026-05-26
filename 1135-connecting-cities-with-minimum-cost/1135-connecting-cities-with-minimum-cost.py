class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in connections:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        total_cost = conneted_city = 0
        pq = [(0, 1)]

        while pq:
            cost, city = heapq.heappop(pq)

            if visited[city]:
                continue

            visited[city] = True
            total_cost += cost
            conneted_city += 1

            for nei, wei in graph[city]:
                heapq.heappush(pq, (wei, nei))

        return total_cost if conneted_city == n else -1

        