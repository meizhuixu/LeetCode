class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # leetcode
        # leet
        # f(code)

        word_set = set(wordDict)
        memo = defaultdict(bool)
        def dfs(s):
            if s in memo:
                return memo[s]
            if s in word_set:
                memo[s] = True
                return True
            for j in range(len(s)):
                if s[0:j] in word_set:
                    if dfs(s[j:]):
                        return True
            memo[s] = False
            return False
        return dfs(s)

        # s: len N
        # dic: len M
        # branch M
        # M^N
        
