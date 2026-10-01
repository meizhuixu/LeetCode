class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # time O(m*n)  space O(m*n)

        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = 0

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '1':
                return

            grid[x][y] = '0'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res
        