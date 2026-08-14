class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # forbidden negative  b * 2
        # bfs

        if x == 0:
            return 0

        queue = deque([(0, 1, 0)])  # posi, dire, count
        visited = set([(0, 1)])
        forbidden_set = set(forbidden)
        limit = max(x, max(forbidden_set)) + a + b

        while queue:
            position, direction, count = queue.popleft()

            nxt_r = position + a
            if nxt_r == x:
                return count + 1
            if nxt_r <= limit and (nxt_r, 1) not in visited and nxt_r not in forbidden_set:
                queue.append((nxt_r, 1, count + 1))
                visited.add((nxt_r, 1))

            if direction == 1:
                nxt_l = position - b
                if nxt_l == x:
                    return count + 1
                if nxt_l >= 0 and (nxt_l, -1) not in visited and nxt_l not in forbidden_set:
                    queue.append((nxt_l, -1, count + 1))
                    visited.add((nxt_l, -1))

        return -1