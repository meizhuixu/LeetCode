class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = (0, 0) # start, length

        def extend(i, j):
            l, r = i, j
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > self.res[1]:
                    self.res = (l, length)
                l -= 1
                r += 1

            return
        
        for i in range(n):
            extend(i, i)
            extend(i, i + 1)

        return s[self.res[0]: self.res[0] + self.res[1]]

        
        