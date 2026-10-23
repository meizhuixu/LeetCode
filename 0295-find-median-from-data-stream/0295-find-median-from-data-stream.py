class MedianFinder:

    def __init__(self):
        self.l = []  # max heap(-)
        self.r = []  # min heap
        
    def addNum(self, num: int) -> None:
        if self.r and num > self.r[0]:
            heapq.heappush(self.r, num)
            if len(self.r) - len(self.l) > 1:
                heapq.heappush(self.l, -heapq.heappop(self.r))
        else:
            heapq.heappush(self.l, -num)
            if len(self.l) - len(self.r) > 1:
                heapq.heappush(self.r, -heapq.heappop(self.l))

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return -self.l[0]
        elif len(self.l) < len(self.r):
            return self.r[0]
        else:
            return (-self.l[0] + self.r[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()