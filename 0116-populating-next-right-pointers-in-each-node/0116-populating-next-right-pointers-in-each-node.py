"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
            
        queue = deque([root])
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                level.append(curr)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            for i in range(len(level) - 1):
                level[i].next = level[i+1]

        return root

        