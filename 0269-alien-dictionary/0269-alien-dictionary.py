class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # topologic
        # 1. build graph: compare each adjacent 2 words
        # 2. topologic: is circle return empty str
        
        word_set = set()
        for word in words:
            for char in word:
                word_set.add(char)

        n = len(words)
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(n - 1):
            length = min(len(words[i]), len(words[i + 1]))
            if words[i][:length] == words[i+1][:length] and len(words[i]) > length:
                return ''

            for j in range(length):
                if words[i][j] == words[i+1][j]:
                    continue
                if words[i+1][j] not in graph[words[i][j]]:
                    graph[words[i][j]].add(words[i+1][j])
                    indegree[words[i+1][j]] += 1
                break

        queue = deque()
        for char in word_set:
            if indegree[char] == 0:
                queue.append(char)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        print(graph)

        return '' if len(res) < len(word_set) else ''.join(res)

            

        

        



                
                
        