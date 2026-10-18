class Solution:
    def minInsertions(self, s: str) -> int:
        need_r = res = 0

        for c in s:
            if c == '(':
                need_r += 2
                if need_r % 2 != 0:  # before is '()'
                    res += 1   # add ')'
                    need_r -= 1  #  update

            if c == ')':
                need_r -= 1
                if need_r < 0:
                    res += 1   # add '('
                    need_r += 2  # need 2 more ')'

        return res + need_r

        