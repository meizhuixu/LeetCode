class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 4 for i in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            # hold
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i], dp[i - 1][3] - prices[i])

            # sell
            dp[i][1] = dp[i - 1][0] + prices[i]

            # cooldown
            dp[i][2] = dp[i - 1][1]

            # not hold
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2])

        return max(dp[-1][1], dp[-1][2], dp[-1][3])