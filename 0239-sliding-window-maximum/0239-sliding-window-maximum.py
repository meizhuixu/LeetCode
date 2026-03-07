class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        l = 0

        for r in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)

            if r - l + 1 > k:
                if queue[0] <= l:
                    queue.popleft()
                l += 1

            if r - l + 1 == k:
                res.append(nums[queue[0]])

        return res



