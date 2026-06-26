"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # bfs
        # edge case: empty root
        
        queue = deque([root])
        res = []
        
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                cur = queue.popleft()
                level.append(cur.val)

                for c in cur.children:
                    queue.append(c)

            res.append(level)


        return res


