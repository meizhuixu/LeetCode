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
        # bfs
        if not node:
            return None

        hashmap = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    queue.append(nei)
                hashmap[curr].neighbors.append(hashmap[nei])

        return hashmap[node]
