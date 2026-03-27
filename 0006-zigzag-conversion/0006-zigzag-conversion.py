class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        res = [''] * numRows
        go_down = False
        cur_row = 0

        for chr in s:
            res[cur_row] += chr

            if cur_row == 0 or cur_row == numRows - 1:
                go_down = not go_down

            cur_row += 1 if go_down else -1

        return ''.join(res)

        