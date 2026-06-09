class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # words = ["wrt","wrf","er","ett","rftt"]
        # t: f
        # w: e
        # r: t
        # e: r


        graph = {}
        indegree = {}

        for word in words:
            for chr in word:
                graph[chr] = set()
                indegree[chr] = 0

        for i in range(len(words) - 1):
            j = 0
            while j < min(len(words[i]), len(words[i + 1])):
                min_len = min(len(words[i]), len(words[i + 1]))
                if len(words[i]) > len(words[i + 1]) and words[i][:min_len] == words[i + 1]:
                    return ''
                if words[i][j] != words[i + 1][j]:
                    if words[i + 1][j] not in graph[words[i][j]]:
                        graph[words[i][j]].add(words[i + 1][j])
                        indegree[words[i + 1][j]] += 1
                    break
                else:
                    j += 1
        print(graph)
        print(indegree)

        queue = deque()
        for key in graph:
            if indegree[key] == 0:
                queue.append(key)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return ''.join(res) if len(res) == len(graph) else ''

        






        