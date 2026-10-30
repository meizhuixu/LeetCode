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
        # dfs
        # dict = {old: new}
        # O(n); O(n)

        # edge case: empty
        self.hashmap = {}
        def dfs(node):
            if not node:
                return None
            if node in self.hashmap:
                return self.hashmap[node]

            new = Node(node.val)
            self.hashmap[node] = new
            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))

            return new

        return dfs(node)


        