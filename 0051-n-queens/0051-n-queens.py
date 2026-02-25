class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        seen_col = set()
        seen_diag1 = set()
        seen_diag2 = set()
        
        
        def backtracking(row):
            if row == n:
                res.append([''.join(line) for line in board])
                return

            for col in range(n):
                if col in seen_col or (row + col) in seen_diag1 or (row - col) in seen_diag2:
                    continue
                seen_col.add(col)
                seen_diag1.add(row + col)
                seen_diag2.add(row - col)
                board[row][col] = 'Q'

                backtracking(row + 1)

                seen_col.remove(col)
                seen_diag1.remove(row + col)
                seen_diag2.remove(row - col)
                board[row][col] = '.'

        backtracking(0)
        return res

        