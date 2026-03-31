"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            cur = node.right
            while cur and cur.left:
                cur = cur.left
            return cur

        if node.parent:
            cur = node
            while cur and cur.parent:
                if cur.parent.left == cur:
                    return cur.parent
                cur = cur.parent
                