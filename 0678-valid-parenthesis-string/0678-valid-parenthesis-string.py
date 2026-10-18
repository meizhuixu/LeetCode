class Solution:
    def checkValidString(self, s: str) -> bool:
        need_r_min = need_r_max = 0

        for c in s:
            if c == '(':
                need_r_min += 1
                need_r_max += 1
            if c == ')':
                need_r_min -= 1
                need_r_max -= 1
            if c == '*':
                need_r_min -= 1   # '*' as ')'
                need_r_max += 1   # '*' as '('

            if need_r_min < 0:
                need_r_min = 0  # turn one '*' from ')' to '('
            if need_r_max < 0:
                return False    # turn all '*' into ')', still not enough

        return True if need_r_min == 0 else False
        