class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in tickets:
            graph[f].append(t)

        for airports in graph.values():
            airports.sort(reverse=True)

        res = []
        def dfs(curr):
            while graph[curr]:
                nxt = graph[curr].pop()
                dfs(nxt)
            res.append(curr)

        dfs('JFK')
        return res[::-1]



