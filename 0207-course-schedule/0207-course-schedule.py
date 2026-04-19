class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(E); O(E + V)
        course_map = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            course_map[b].append(a)
            in_degree[a] += 1

        # O(V); O(V)
        queue = deque()
        for c, num in enumerate(in_degree):
            if num == 0:
                queue.append(c)

        # O(E + V); O(V)
        count = 0
        while queue:
            cur = queue.popleft()
            count += 1

            for nei in course_map[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        # check circle
        return count == numCourses