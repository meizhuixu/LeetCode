class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        # dist = [w]    dist to reach node i is dist[i] time
        # pq [(0, k)]  (node, the minimum time to reach node)

        # times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = [float('inf')] * (n + 1)   # [++, 1, 0]
        pq = [(0, k)] # 

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            dist[node] = time
            for dt, nxt in graph[node]:
                if dist[nxt] > time + dt:
                    heapq.heappush(pq, (time + dt, nxt))

        res = max(dist[i] for i in range(1, n + 1))
        print(dist)
        return res if res != float('inf') else -1
        


        