"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []

        def traversal(node):
            if not node:
                return

            self.res.append(node.val)
            for c in node.children:
                traversal(c)

        traversal(root)
        return self.res

        