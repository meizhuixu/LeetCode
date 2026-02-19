class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # Pruning
        if len(word) > m * n:
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y, idx):
            # Success condition: all characters in the word have been matched
            if idx == len(word):
                return True

            # Boundary check and character validation
            # Also ensures we don't revisit the same cell in the current path ('#')
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx]:
                return False

            # Mark the current cell as visited to prevent reuse
            temp_char = board[x][y]
            board[x][y] = '#'
            
            # Explore all four adjacent directions
            for dx, dy in directions:
                if dfs(x + dx, y + dy, idx + 1):
                    return True
            
            # Backtrack: restore the original character for other paths
            board[x][y] = temp_char
            return False

        # Iterate through every cell in the grid as a potential starting point
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False