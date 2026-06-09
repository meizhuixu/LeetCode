class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        indegree = {}
        for word in words:
            for chr in word:
                graph[chr] = set()
                indegree[chr] = 0
        

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ''

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        print(indegree)

        queue = deque()
        for chr, num in indegree.items():
            if num == 0:
                queue.append(chr)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return ''.join(res) if len(res) == len(indegree) else ''