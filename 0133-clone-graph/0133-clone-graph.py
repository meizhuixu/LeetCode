"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case: node is None/nei is None
        if not node:
            return None

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            new = Node(node.val)
            old_to_new[node] = new

            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))
            return new

        old_to_new = dict()
        return dfs(node)