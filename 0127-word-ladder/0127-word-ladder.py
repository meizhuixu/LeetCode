class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs -> shortest path
        # hit -> *it h*t hi* -> in wordlist
        # wordlist -> wordset  O(1)
        # find endword -> return step
        # return 0: 1. endword not in wordlist  2. during search -> no new word in wordlist
        # time: O(n * n * m)     n = len(word)   m = len(wordlist)
        # space: O(n * m)

        wordSet = set(wordList)
        # pruning
        if endWord not in wordSet:
            return 0

        path = set([beginWord])
        queue = deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    new_word = ''.join(word_list)  # O(n)
                    if new_word in path:
                        continue
                    if new_word == endWord:
                        return step + 1
                    if new_word in wordSet:
                        path.add(new_word)
                        queue.append((new_word, step + 1))

        return 0



        