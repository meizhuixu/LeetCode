class Solution:
    def checkValidString(self, s: str) -> bool:
        # ( +1
        # ) -1
        # max_left  +1  -> False
        # min_left  -1  -> 

        # return min_left == 0

        min_l = max_l = 0
        for chr in s:
            if chr == '(':
                max_l += 1
                min_l += 1
            elif chr == ')':
                max_l -= 1
                min_l -= 1

            elif chr == '*':
                max_l += 1
                min_l -= 1

            if max_l < 0:
                return False
            if min_l < 0:
                min_l = 0

        return min_l == 0

        