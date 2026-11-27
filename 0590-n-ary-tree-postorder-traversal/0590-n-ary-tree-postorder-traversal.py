"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traversal(node):
            if not node:
                return

            for c in node.children:
                traversal(c)

            res.append(node.val)
            return

        res = []
        traversal(root)
        return res
        

        