class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1) # dist to k
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        # build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        while pq:
            d, cur = heapq.heappop(pq)
            for nxt_d, nei in graph[cur]:
                if dist[nei] > d + nxt_d:
                    dist[nei] = d + nxt_d
                    heapq.heappush(pq, (dist[nei], nei))

        res = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            res = max(res, dist[i])

        return res
 


        