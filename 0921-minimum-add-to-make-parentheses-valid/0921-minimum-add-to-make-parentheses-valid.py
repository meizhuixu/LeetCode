class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need_r = res = 0

        for c in s:
            if c == '(':
                need_r += 1
            if c == ')':
                need_r -= 1
                if need_r < 0:
                    res += 1
                    need_r = 0

        return res + need_r