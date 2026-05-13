class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1[i] == word2[j]
        # dp[i][j] = dp[i - 1][j - 1]
        # !=
        # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        m, n = len(word1), len(word2)
        dp = [i for i in range(n + 1)]

        for i in range(1, m + 1):
            prev = i - 1
            for j in range(n + 1):
                if j == 0:
                    dp[j] = i
                else:
                    curr = dp[j]
                    if word1[i - 1] == word2[j - 1]:
                        dp[j] = prev
                    else:
                        dp[j] = min(dp[j], dp[j - 1]) + 1
                    prev = curr

        return dp[-1]
        