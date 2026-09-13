class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph and indegree
        graph = defaultdict(list)  #  from: [to]
        indegree = defaultdict(int) # course: num
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # find all courses without indegree
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # bfs
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return count == numCourses



