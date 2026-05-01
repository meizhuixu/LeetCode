class Solution:
    def numSquares(self, n: int) -> int:
        # i = 1, 2...   while i * i <= n:
        # dp[j] = least number of ps numbers that sum to j
        # dp[j] = min(dp[j], dp[j - i * i] + 1)
        # n = 12

        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        i = 1
        while i * i <= n: 
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)

            i += 1

        return dp[-1]

    
        