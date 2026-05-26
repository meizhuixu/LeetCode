class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        visited = {}
        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited[node] = time
            for nxt, dt in graph[node]:
                heapq.heappush(pq, (time + dt, nxt))

        return max(visited.values()) if len(visited) == n else -1