class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y, old, new):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != old:
                return

            board[x][y] = new
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                dfs(nx, ny, old, new)

        # first pass: iterate through 4 boundaries, replace 'O' with 'Y'
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0, 'O', 'Y')
            if board[i][n - 1] == 'O':
                dfs(i, n - 1, 'O', 'Y')

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j, 'O', 'Y')
            if board[m - 1][j] == 'O':
                dfs(m - 1, j, 'O', 'Y')

        # second pass: convert all 'O' to 'X'; convert 'Y' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

        return