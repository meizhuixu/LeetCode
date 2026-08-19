class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs 
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses
        # 0: unvisit   1: visiting   2: visited
        # 0   1  2  3
        def dfs(c):
            if visited[c] == 1:
                return False
            if visited[c] == 2:
                return True

            visited[c] = 1
            for nxt in graph[c]:
                if not dfs(nxt):
                    return False
            visited[c] = 2
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
