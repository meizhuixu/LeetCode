class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y, idx):
            # base case
            if idx == len(word):
                return True

            # check if can enter next dfs
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx] or board[x][y] == '#':
                return

            chr = board[x][y]
            board[x][y] = '#'
            for dx, dy in directions:
                if dfs(x+dx, y+dy, idx+1):
                    return True
            board[x][y] = chr

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

        

            
        