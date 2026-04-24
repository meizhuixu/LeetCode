class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # To solve this problem, I'll use a 2D dynamic programming array, dp[i][j], to represent the length of the longest palindromic subsequence within the substring from index i to index j
        dp = [[0] * n for _ in range(n)]

        # Since dp[i][j] depends on dp[i+1], which is the next row, we need to iterate i in reverse order (from n-1 down to 0)
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
        # For each i, we iterate j forward from i+1 to ensure we always have the 'left' and 'bottom' values already computed
            for j in range(i + 1, n):
                # If the characters at both ends are the same, they can form part of the palindrome. So, dp[i][j] will be dp[i+1][j-1] + 2. We take the result from the inner substring and add two for the matching characters
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # If they don't match, the longest subsequence must come from either excluding the first character or excluding the last character. Thus, we take the maximum of dp[i+1][j] and dp[i][j-1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][-1]
        