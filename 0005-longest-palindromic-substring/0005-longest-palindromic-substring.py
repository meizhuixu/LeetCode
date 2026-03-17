class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = (float('-inf'), float('-inf'))  #  idx and length

        for i in range(n):
            # single letter
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > res[1]:
                    res = (l, r - l + 1)
                l -= 1
                r += 1

            # double letters
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > res[1]:
                    res = (l, r - l + 1)
                l -= 1
                r += 1

        return s[res[0]: res[0] + res[1]]
        
        