# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def postorder(node):
            if not node:
                return 0

            left = postorder(node.left)
            right = postorder(node.right)
            diameter = left + right
            self.max_diameter = max(self.max_diameter, diameter)
            return max(left, right) + 1

        postorder(root)
        return self.max_diameter

        