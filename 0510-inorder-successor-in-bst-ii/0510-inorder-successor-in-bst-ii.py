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
        # if node has right sub-tree
        if node.right:
            cur = node.right
            while cur and cur.left:
                cur = cur.left
            return cur

        # if node has no right sub-tree, search for its parent
        cur = node
        while cur.parent and cur.parent.right == cur:
            cur = cur.parent

        return cur.parent
                