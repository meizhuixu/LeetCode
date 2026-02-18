class TrieNode:
    def __init__(self):
        self.children = {} # {chr: TrieNode}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        # 'bad'
        node = self.root # start from root
        for chr in word:
            if chr not in node.children:
                node.children[chr] = TrieNode()
            node = node.children[chr]
        node.is_end = True # mark a word ending  
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
                
            chr = word[idx]
            if chr == '.':
                for next_node in node.children.values():
                    if dfs(next_node, idx + 1):
                        return True
                return False
            else:
                if chr not in node.children:
                    return False
                return dfs(node.children[chr], idx + 1)
                
        return dfs(self.root, 0)
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)