class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # simulation/pq
        # pq = [-3, -3]   pop the most freq task
        # queue = [(-2, 4), (-2, 5)]  FIFO the first task back to pq

        hashmap = Counter(tasks)
        pq = []
        for freq in hashmap.values():
            heapq.heappush(pq, -freq)

        queue = deque()
        time = 0
        while pq or queue:
            time += 1
            if pq:
                neg_freq = heapq.heappop(pq)
                if neg_freq < -1:
                    queue.append((neg_freq + 1, time + n))

            if queue and queue[0][1] == time:
                neg_freq, _ = queue.popleft()
                heapq.heappush(pq, neg_freq)

        return time


    
        