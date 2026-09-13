class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs: no cycle
        # build graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course, path):
            if path[course] == 1:
                return False
            if path[course] == 2:
                return True
            
            path[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt, path):
                    return False
            path[course] = 2

            return True

        path = [0] * numCourses # 0:unvisited  1: visiting  2: visited
        for i in range(numCourses):
            if not dfs(i, path):
                return False

        return True

        