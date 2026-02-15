class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x < y:
                heapq.heappush(pq, x - y)

        return -pq[0] if pq else 0

        