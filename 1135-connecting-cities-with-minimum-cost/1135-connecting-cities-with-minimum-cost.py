class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # connect n nodes, at least (n - 1) edges
        if len(connections) < n - 1:
            return -1

        # n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
        # pq = [(1, 3), (6, 3) ]   cost, next
        # visited = [False] * (n + 1)
        # total_cost = 5 + 1 = 6

        # build graph
        # time O(E)  space O(V + E)
        graph = defaultdict(list)
        for x, y, cost in connections:
            graph[x].append((cost, y))
            graph[y].append((cost, x))

        visited = [False] * (n + 1)   # 1 -> n
        total_cost = connected_city = 0
        pq = [(0, 1)]

        # time O(ElogV) space O(E)
        # E = V**2
        # logE = 2logV
        while pq:
            cost, node = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            total_cost += cost
            connected_city += 1

            for cost, nxt in graph[node]:
                if not visited[nxt]:
                    heapq.heappush(pq, (cost, nxt))

        return total_cost if connected_city == n else -1

        # time O(ElogV) space O(V + E)




        