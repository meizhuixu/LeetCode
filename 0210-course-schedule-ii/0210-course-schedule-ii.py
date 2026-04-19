class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph and indegree
        in_degree = [0] * numCourses
        course_map = defaultdict(list)
        for a, b in prerequisites:
            in_degree[a] += 1
            course_map[b].append(a)

        # find all course without prerequisites
        queue = deque()
        for c, count in enumerate(in_degree):
            if count == 0:
                queue.append(c)


        # bfs: take all courses without prerequisites, neighbors indegree decrement by 1, if indegree == 0, put them into queue
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for nei in course_map[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return res if len(res) == numCourses else []
