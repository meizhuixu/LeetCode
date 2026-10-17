class Solution:
    def checkValidString(self, s: str) -> bool:
        # left to right, '*' as '('
        need_r = 0
        for c in s:
            if c == ')':
                need_r -= 1
            else:
                need_r += 1

            if need_r < 0:
                return False

        need_l = 0
        for c in s[::-1]:
            if c == '(':
                need_l -= 1
            else:
                need_l += 1

            if need_l < 0:
                return False

        return True


        