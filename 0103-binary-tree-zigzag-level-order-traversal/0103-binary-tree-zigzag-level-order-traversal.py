# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        left_to_right = True
        queue = deque([root])
        res = []

        while queue:
            length = len(queue)
            level = []

            for _ in range(length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                if not left_to_right:
                    level.reverse()
                res.append(level)
                left_to_right = not left_to_right

        return res