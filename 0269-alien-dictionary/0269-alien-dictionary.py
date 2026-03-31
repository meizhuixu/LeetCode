class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # initiate graph and in_degree
        graph = {}
        for word in words:
            for chr in word:
                graph[chr] = set()

        in_degree = {}
        for chr in graph:
            in_degree[chr] = 0

        # build graph and in_degree
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # 'abb' and 'ab' are ineligible
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ''

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # put all zero indegree character into queue
        queue = deque()
        for chr, freq in in_degree.items():
            if freq == 0:
                queue.append(chr)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for nei in graph[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return ''.join(res) if len(res) == len(graph) else ''


            