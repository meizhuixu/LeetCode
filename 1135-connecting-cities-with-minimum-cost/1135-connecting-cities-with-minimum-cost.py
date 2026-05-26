class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # time O(E); space O(V + E)
        graph = defaultdict(list)
        for u, v, w in connections:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1) # space O(V)
        total_cost = conneted_city = 0
        pq = [(0, 1)]

        while pq:
            cost, city = heapq.heappop(pq) # time O(ElogV)

            if visited[city]:
                continue

            visited[city] = True
            total_cost += cost
            conneted_city += 1

            for nei, wei in graph[city]: # time O(ElogV)
                heapq.heappush(pq, (wei, nei))

        return total_cost if conneted_city == n else -1

        