class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # sliding window
        # time O(n)  space O(1)

        l = total = 0
        res = - float('inf')

        for r in range(len(nums)):
            total += nums[r]
            if total < nums[r]:
                l = r
                total = nums[r]

            res = max(res, total)

        return res

        