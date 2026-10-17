class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = left = 0

        for chr in s:
            if chr == ')':
                if left > 0:
                    left -= 1
                else:
                    res += 1
            else:
                left += 1

        return res + left
        