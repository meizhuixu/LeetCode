class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for chr in word:
            node = node.children[chr]

        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self._find(prefix)
        return node is not None


    def _find(self, prefix):
        node = self.root
        for chr in prefix:
            if chr not in node.children:
                return None
            node = node.children[chr]

        return node
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)