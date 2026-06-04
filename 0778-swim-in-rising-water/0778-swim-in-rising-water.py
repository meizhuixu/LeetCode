class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = max(grid[0][0], grid[-1][-1])
        pq = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while pq:
            val, x, y = heapq.heappop(pq)
            visited[x][y] = True
            if val > res:
                res = val

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx == n - 1 and ny == n - 1:
                    return res
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))

        return res

        



        