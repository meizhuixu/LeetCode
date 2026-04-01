class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create graph {u: [(w, v)]} record directionnal edges from one vertex
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        # create array to store minimum time from k
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # initiate a heap to do bfs
        pq = []
        heapq.heappush(pq, (0, k)) # add origin k
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            
            for w, v in graph[node]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        total_time = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            total_time = max(total_time, dist[i])

        return total_time