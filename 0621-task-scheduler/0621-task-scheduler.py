class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = [-val for val in Counter(tasks).values()]
        heapq.heapify(pq)

        queue = deque()
        time = 0
        while pq or queue:
            time += 1

            if pq:
                freq = heapq.heappop(pq)
                freq += 1
                if freq < 0:
                    queue.append((freq, time + n))

            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(pq, freq)

        return time

        