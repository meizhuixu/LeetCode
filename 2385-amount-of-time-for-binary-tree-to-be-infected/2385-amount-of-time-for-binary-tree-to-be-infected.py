# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # build graph
        hashmap = defaultdict(list)
        visited = set()

        def build(node):

            if node.right:
                hashmap[node.val].append(node.right.val)
                hashmap[node.right.val].append(node.val)
                build(node.right)

            if node.left:
                hashmap[node.val].append(node.left.val)
                hashmap[node.left.val].append(node.val)
                build(node.left)

        build(root)

        # infection
        queue = deque([start])
        res = -1
        visited = set([start])
        while queue:
            length = len(queue)
            res += 1
            for _ in range(length):
                cur = queue.popleft()
                visited.add(cur)

                for nei in hashmap[cur]:
                    if nei not in visited:
                        queue.append(nei)

        return res