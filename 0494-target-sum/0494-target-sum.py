class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #  -sum <=   <= sum
        # abs(target) > sum: return 0
        # left + right = sum
        # left - right = target -> left
        # dp[i] : numbers of expressions sum == i
        # for num in nums:
        # for i in range(left, num - 1, -1):
        # return dp[-1]
        
        if abs(target) > sum(nums) or (sum(nums) + target) % 2 == 1:
            return 0
        total = (sum(nums) + target) // 2

        dp = [0] * (total + 1)
        dp[0] = 1
        for num in nums:
            for i in range(total, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[-1]

        