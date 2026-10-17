class Solution:
    def minInsertions(self, s: str) -> int:
        need_r = res = 0

        for chr in s:
            if chr == '(':
                need_r += 2
                if need_r % 2 == 1:
                    res += 1
                    need_r -= 1

            if chr == ')':
                need_r -= 1
                if need_r < 0:
                    res += 1
                    need_r += 2

        return res + need_r









        