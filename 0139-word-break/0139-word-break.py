class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if s[j: i] in wordDict and dp[j]:
                    dp[i] = True

        return dp[-1]

        # time: O(n * n)  n = len(s)
        # space: O(n)