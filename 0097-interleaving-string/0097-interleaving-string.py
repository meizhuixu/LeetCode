class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        
        # s1[i] == s3[i + j] and dp[i - 1][j]: dp[i][j] = True
        # s2[j] == s3[i + j]
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif j == 0:
                    dp[i][j] = s1[i - 1] == s3[i - 1] and dp[i - 1][j]
                elif i == 0:
                    dp[i][j] = s2[j - 1] == s3[j - 1] and dp[i][j - 1]
                elif i > 0 and j > 0:
                    dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])


        return dp[-1][-1]
         