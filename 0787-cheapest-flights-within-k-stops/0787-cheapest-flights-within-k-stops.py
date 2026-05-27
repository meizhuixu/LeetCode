class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]
            updated = False

            for u, v, w in flights:
                if dist[u] != float('inf') and temp[v] > dist[u] + w:
                    temp[v] = dist[u] + w
                    updated = True

            if not updated:
                break

            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1