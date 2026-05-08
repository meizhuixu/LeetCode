class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        
        # s1[i] == s3[i + j] and dp[i - 1][j]: dp[i][j] = True
        # s2[j] == s3[i + j]
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m):
            if s1[i] == s3[i]:
                dp[i + 1][0] = True
            else:
                break
        for j in range(n):
            if s2[j] == s3[j]:
                dp[0][j + 1] = True
            else:
                break

        # s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]
         