class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = (0, 0)  #  idx and length

        def extend(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > self.res[1]:
                    self.res = (l, r - l + 1)
                l -= 1
                r += 1

        for i in range(n):
            # single letter
            extend(i, i)

            # double letters
            extend(i, i + 1)

        return s[self.res[0]: self.res[0] + self.res[1]]
        
        