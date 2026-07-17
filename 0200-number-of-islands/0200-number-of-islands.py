class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return

            grid[x][y] = '0'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(x + dx, y + dy)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res
        