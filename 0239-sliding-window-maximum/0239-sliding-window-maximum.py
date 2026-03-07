class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a decreasing monotonic queue
        # add new number into right (min), pop all the smaller number
        # pop a number from left(max)
        # nums = [1, 3,-1,-3,5,3,6,7], k = 3
        #                      l   r
        # queue = [7]
        # res = [3, 3, 5, 5, 6, 7]
        # time: O(n) n = len(nums)
        # space: O(k) 

        res = []
        l = 0
        queue = deque()
        
        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if r - l + 1 > k:
                if l == queue[0]:
                    queue.popleft()
                l += 1

            if r - l + 1 == k:
                res.append(nums[queue[0]])

        return res
        