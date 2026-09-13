class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph and indegree  time O(E)
        graph = defaultdict(list)  #  from: [to]   space O(V + E)
        indegree = defaultdict(int) # course: num    space O(V)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # find all courses without indegree  time O(V)
        queue = deque()   # space O(V)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # bfs  time O(V + E)
        count = 0
        while queue: 
            curr = queue.popleft()
            count += 1

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return count == numCourses



