class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topologic 
        # indegree array: [1, 2]
        # idx: course   num: prereq number of this cours   ==0  -> take
        # dict: {1: [2, 3]}
        # key: course i   value: list of courses whose prereq is i
        # bfs: put course (indgree == 0) into a queue
        # pop c , iterater through dict[c], indegree[nei] -= 1
        # indegree[nei] == 0 -> put into the queue
        # queue is empty  , check the number of courses  == numCourse -> True
        # -> False
        # time: O(E + V)
        # space: O(V + E)

        indegree = [0] * numCourses
        hashmap = defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            hashmap[b].append(a)

        queue = deque()
        for i, num in enumerate(indegree):
            if num == 0:
                queue.append(i)

        total = 0
        while queue:
            cur = queue.popleft()
            total += 1

            for nei in hashmap[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return total == numCourses



        