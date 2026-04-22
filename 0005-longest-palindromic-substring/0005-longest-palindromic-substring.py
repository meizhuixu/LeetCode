class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1 chr
        # 2 chr: same

        # iterate s
        # start from s[i]:
        # 1 chr 
        # 2 chr : if s[i] == s[i + 1]
        # res: store longest length
        # s = "babad"
        # s = "cbbd"
        # time: O(n*n) n = len(s)
        # space: O(1)

        def extend(i, j):
            l, r = i, j
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r)

        n = len(s)
        res = (0, 0, 0)

        for i in range(n):
            l, r = extend(i, i)
            if r - l > res[0]:
                res = (r - l, l , r)

            if i < n - 1:
                l, r = extend(i, i + 1)
                if r - l > res[0]:
                    res = (r - l, l, r)
            

        return s[res[1]: res[2]]


        