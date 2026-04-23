class Solution:
    def countSubstrings(self, s: str) -> int:
        # iterate each char in s
        # extend from 1 char or 2 char
        # palind: extend 
        # time: O(n*n)
        # space: O(1)

        self.count = 0
        n = len(s)

        def extend(i, j):
            l, r = i, j
            while l >= 0 and r < n and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
            return

        for i in range(n):
            extend(i, i)
            extend(i, i + 1)

        return self.count



        