class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        cur = self.root
        for char in string:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = string

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(x, y, node, visited):
            if node.word:
                res.append(node.word)
                node.word = None
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or board[x][y] not in node.children:
                return

            node = node.children[board[x][y]]
            visited.add((x, y))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                dfs(nx, ny, node, visited)
            visited.remove((x, y))

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                visited = set()
                dfs(i, j, trie.root, visited)

        return res
        