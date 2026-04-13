class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return

            self.area += 1
            grid[x][y] = 0
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    res = max(res, self.area)

        return res

