class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        n = len(word)
        
        def dfs(node, idx):
            if idx == n:
                return node.is_end

            if word[idx] == '.':
                for c, nxt in node.children.items():
                    if dfs(nxt, idx + 1):
                        return True
                return False
            else:
                if word[idx] not in node.children:
                    return False
                return dfs(node.children[word[idx]], idx + 1)


        return dfs(self.root, 0)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)