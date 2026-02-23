class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            word, count = queue.popleft()

            for i in range(len(word)):
                word_list = list(word)

                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    new_word = ''.join(word_list)

                    if new_word == endWord:
                        return count + 1
                    if new_word not in visited and new_word in wordSet:
                        visited.add(new_word)
                        queue.append((new_word, count + 1))

        return 0

        