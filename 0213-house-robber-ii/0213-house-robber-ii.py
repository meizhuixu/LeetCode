class Solution:
    def rob(self, nums: List[int]) -> int:
        def robLine(nums):
            n = len(nums)
            if n == 1:
                return nums[0]

            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]

        if len(nums) == 1:
            return nums[0]

        return max(robLine(nums[:-1]), robLine(nums[1:]))
        