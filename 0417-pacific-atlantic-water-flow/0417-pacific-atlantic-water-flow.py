class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # search from each edge side
        # two sets for each ocean: store the grid could flow to this ocean
        # intersection 
        # how to search: dfs 
        # time: O(r * c)
        # space: O(r * c)

        set_p, set_a = set(), set()
        m, n = len(heights), len(heights[0])

        def dfs(x, y, ocean):
            ocean.add((x, y))

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in ocean:
                    continue
                if heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, ocean)


        for i in range(m):
            dfs(i, 0, set_p)
            dfs(i, n - 1, set_a)

        for j in range(n):
            dfs(0, j, set_p)
            dfs(m - 1, j, set_a)


        return [list(pair) for pair in set_p & set_a]