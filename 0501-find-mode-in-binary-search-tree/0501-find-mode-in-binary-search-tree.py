# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        self.mode = []
        self.prev = None
        self.count = self.max_count = 0

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if node.val == self.prev:
                self.count += 1
            else:
                self.prev = node.val
                self.count = 1

            if self.count == self.max_count:
                self.mode.append(node.val)
            elif self.count > self.max_count:
                self.max_count = self.count
                self.mode = [node.val]

            inorder(node.right)

        inorder(root)
        return self.mode

        