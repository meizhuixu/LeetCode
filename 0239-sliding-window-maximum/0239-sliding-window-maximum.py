class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue: big -> small
        queue = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            # add nums[r] into decreasing queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # ensure the size of sliding window <= k
            if r - l + 1 > k:
                l += 1
                if queue[0] < l:
                    queue.popleft()

            # add maximum into res when size == k
            if r - l + 1 == k:
                res.append(nums[queue[0]])

        return res

            




        