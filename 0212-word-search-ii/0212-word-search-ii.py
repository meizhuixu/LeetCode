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
            # base case, no return here
            if node.word:
                res.append(node.word)
                node.word = None
            
            # check border
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            # check there is a route or not visited
            chr = board[x][y]
            if chr not in node.children or chr == '#':
                return

            # backtracking
            board[x][y] = '#'
            for dx, dy in directions:
                backtracking(x+dx, y+dy, node.children[chr])
            board[x][y] = chr


        for i in range(m):
            for j in range(n):
                backtracking(i, j, root)

        return res

            

            
        