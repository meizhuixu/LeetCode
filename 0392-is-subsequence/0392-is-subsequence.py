class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False

        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                curr = dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = dp[j - 1]
                prev = curr

        return dp[-1] == m