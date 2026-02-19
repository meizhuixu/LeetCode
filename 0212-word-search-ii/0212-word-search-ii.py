class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct Trie
        root = TrieNode()
        for word in words:
            node = root
            for chr in word:
                if chr not in node.children:
                    node.children[chr] = TrieNode()
                node = node.children[chr]
            node.word = word

        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []

        # dfs & backtracking
        def backtracking(x, y, node):
            chr = board[x][y]
            if chr not in node.children:
                return
            next_node = node.children[chr]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[x][y] = '#'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    backtracking(nx, ny, next_node)
            board[x][y] = chr


        for i in range(m):
            for j in range(n):
                backtracking(i, j, root)

        return res

            

            
        