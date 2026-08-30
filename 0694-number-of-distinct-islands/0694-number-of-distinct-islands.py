class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 1. iterate through matrix
        # 2. meet 1: dfs， set 1 to 0
        # store each relative coordinate of adjacent 1
        # 3. return length of res set

        m, n = len(grid), len(grid[0])
        set_res = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(x, y, ox, oy):
            grid[x][y] = 0
            set_island.add((x-ox, y-oy))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx-ox, ny-oy) not in set_island and grid[nx][ny] == 1:
                    dfs(nx, ny, ox, oy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    set_island = set()
                    dfs(i, j, i, j)
                    print(set_island)
                    set_res.add(tuple(set_island))

        return len(set_res)



        