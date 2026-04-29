class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]: largest subset of i * '0' and j * '1'
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str in strs:
            count_0, count_1 = 0, 0
            for chr in str:
                if chr == '0':
                    count_0 += 1
                if chr == '1':
                    count_1 += 1
            
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - count_0][j - count_1] + 1)

        return dp[-1][-1]