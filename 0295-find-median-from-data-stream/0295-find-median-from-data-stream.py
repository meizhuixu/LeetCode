class MedianFinder:

    def __init__(self):
        self.max_heap = [] # add -num
        self.min_heap = [] # add num
        

    def addNum(self, num: int) -> None:
        if self.max_heap and num > -self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            cur = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, cur)
        elif len(self.min_heap) - len(self.max_heap) > 0:
            cur = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -cur)


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        else:
            return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()