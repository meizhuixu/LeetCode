class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # edge case: nums could be empty
        self.pq = []
        self.size = k

        for num in nums:
            heapq.heappush(self.pq, num)
            if len(self.pq) > self.size:
                heapq.heappop(self.pq)
        return
        

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.size:
            heapq.heappop(self.pq)

        return self.pq[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# [10, 9, 8, 5, 5, 4, 4, 3, 2]
# min heap -> return heap[0]
# O(n); O(n)
# O(logk); O(1)
# add n elements: O(nlogk); O(n)