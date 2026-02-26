class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # there is no fresh orange -> 0
        # there is no rotten orage -> -1
        # there is both -> povitive int or -1
        # bfs
        # queue : put all rotten into it
        # count the number of fresh orange
        # bfs: count time -> each time deal with all the rotten orange -> add 1 to time...
        # rotten: 4-dictions fresh orange (1->2) & fresh - 1 & put the new rotten into queue
        # queue is empty: fresh = 0? return time . fresh > 0 -> -1
        
        # iterate matrix to count fresh and put rotten into queue
        queue = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
                    
        if fresh == 0:
            return 0
        if not queue:
            return -1
            
        time = 0
        while queue:
            time += 1
            length = len(queue)
            for _ in range(length):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        if fresh == 0:
                            return time
                        queue.append((nx, ny))
                        
        return -1
                        
                    
        
                    
        