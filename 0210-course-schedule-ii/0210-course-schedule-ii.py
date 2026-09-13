class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        path = [0] * numCourses  # 0: unvisited  1: visiting  2: visited
        res = []
        def dfs(course):
            if path[course] == 1:
                return False
            if path[course] == 2:
                return True

            path[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            path[course] = 2  # 一开始漏写了
            res.append(course)
            return True

        for i in range(numCourses):
            if path[i] == 0:
                if not dfs(i):

                    return []

        return res[::-1]

        
        