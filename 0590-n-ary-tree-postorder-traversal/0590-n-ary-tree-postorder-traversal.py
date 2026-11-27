"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None

        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()

            if not visited and node.children:
                stack.append((node, True))
                for c in node.children[::-1]:
                    stack.append((c, False))
            else:
                res.append(node.val)

        return res

