class TrieNode:
    def __init__(self):
        self.children = {}  # Map: {char: TrieNode}
        self.word = None    # Stores the full string when a word is completed

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Construct Trie: Pre-process vocabulary for efficient prefix lookups
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        m, n = len(board), len(board[0])
        res = []

        # DFS with Backtracking
        def backtracking(x, y, node):
            # Check for word completion at the beginning of the DFS call
            if node.word:
                res.append(node.word)
                node.word = None # Avoid duplicate entries in the result list

            # Boundary Check: Ensure coordinates are within board limits
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            
            # Pruning & Visit Check: Stop if the character isn't in Trie or cell is visited
            char = board[x][y]
            if char not in node.children or char == '#':
                return
            
            # Mark cell as visited to prevent re-use in the current path
            board[x][y] = '#'
            
            # Explore all 4 adjacent directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                backtracking(x + dx, y + dy, node.children[char])
                
            # Backtrack: Restore the cell's original character for other paths
            board[x][y] = char

        # Initiate search from every cell on the board
        for i in range(m):
            for j in range(n):
                # Start DFS only if the first character matches a Trie root child
                if board[i][j] in root.children:
                    backtracking(i, j, root)

        return res