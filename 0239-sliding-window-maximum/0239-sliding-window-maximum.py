class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = 0
        res = []
        queue = deque()

        for r in range(len(nums)):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            if r - l + 1 > k:
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1

            if r - l + 1 == k:
                res.append(queue[0])

        return res



