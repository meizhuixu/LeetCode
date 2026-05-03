class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    length = max(length, dp[j])
            dp[i] = length + 1

        return max(dp)
