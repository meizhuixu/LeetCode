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
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)

            for c in curr.children:
                stack.append(c)

        return res[::-1]

