class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        in_degree = defaultdict(int)
        for a, b in prerequisites:
            course_map[b].append(a)
            in_degree[a] += 1

        queue = deque()
        for c in range(numCourses):
            if in_degree[c] == 0:
                queue.append(c)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for nei in course_map[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        # check circle
        return True if len(res) == numCourses else False