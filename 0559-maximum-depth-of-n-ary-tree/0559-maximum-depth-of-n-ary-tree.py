"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # empty root
        # dfs time O(n)  space O(h)
        self.max_depth = 0
        
        def dfs(node, depth):
            if not node:
                return

            self.max_depth = max(self.max_depth, depth + 1)
            for c in node.children:
                dfs(c, depth + 1)

        dfs(root, 0)
        return self.max_depth

