class Solution:
    def longestPalindrome(self, s: str) -> str:
        # iterate , helper to check longest
        # helper: expand to left and right
        # odd: start from  n, n
        # even: start from n, n+1
        # return   start, end

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = [l, r]
                l -= 1
                r += 1
            return res

        longest = [0, -1] # length, start
        for i in range(len(s)):
            l, r = helper(i, i)
            if r - l + 1 > longest[0]:
                longest = [r - l + 1, l]

            if i < len(s) - 1 and s[i] == s[i+1]:
                l, r = helper(i, i+1)
                if r - l + 1 > longest[0]:
                    longest = [r - l + 1, l]

        return s[longest[1]: longest[1] + longest[0]]

