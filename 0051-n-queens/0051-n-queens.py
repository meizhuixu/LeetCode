class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # edge case: no such solution
        # initiate an empty board with '.'
        # 4 sets: (row), col, diag * 2
        # row:  row idx
        # x, y :  sum of x, y   or   difference of x, y
        # backtracking: 
        #  iterate through each grid in one line


        col, diag_1, diag_2 = set(), set(), set()
        board = [['.'] * n for i in range(n)]
        res = []
        def backtracking(r):
            # base case
            if r == n:
                res.append([''.join(board[i]) for i in range(n)])

            for c in range(n):
                if c in col or (r + c) in diag_1 or (r - c) in diag_2:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                diag_1.add(r + c)
                diag_2.add(r - c)

                backtracking(r + 1)

                board[r][c] = '.'
                col.remove(c)
                diag_1.remove(r + c)
                diag_2.remove(r - c)

        backtracking(0)
        return res

        

                    


