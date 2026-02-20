class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # pruning
        m = len(board)
        n = len(board[0])
        if len(word) > m * n:
            return False
            
        # dfs
        def dfs(x, y, idx):
            # base case: find the word
            if idx == len(word):
                return True
                
            # check boundary; check visited
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx]:
                return False
            
            # backtracking & dfs    
            chr = board[x][y]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                board[x][y] = '#'
                if dfs(x+dx, y+dy, idx+1):
                    return True
                board[x][y] = chr
            return False
            
        
        # iterate through the board
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True     
        return False
        