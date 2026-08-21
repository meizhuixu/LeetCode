class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window & queue(decreasing)
        # nums = [1,3,-1,-3,5,3,6,7], k = 3
        #             (      ) 
        # queue = [5]
        # time: O(n)  space: O(n)
        queue = deque()
        l = 0
        res = []

        for r in range(len(nums)):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            if r - l + 1 > k:
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1

            if r - l + 1 == k:
                res.append(queue[0])

        return res

        



        