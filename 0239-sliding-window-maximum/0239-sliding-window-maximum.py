class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # monotonic queue
        # [6]
        # old -> new
        # big -> small
        # time O(n)
        # space O(n)

        queue = deque()
        l = 0
        res = []

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

            


        