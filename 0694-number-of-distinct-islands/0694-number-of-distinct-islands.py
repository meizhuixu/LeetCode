class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x, y, path):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0: 
                return

            grid[x][y] = 0
            for direction, pair in {'u': (0, 1), 'd': (0, -1), 'r': (1, 0), 'l': (-1, 0)}.items():
                dx, dy = pair
                path.append(direction)
                dfs(x + dx, y + dy, path)

        m, n = len(grid), len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path)
                    res.add(''.join(path))
                
        return len(res)
        