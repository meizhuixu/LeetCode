# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True

            left = dfs(node.left)

            if node.val <= self.max_val:
                return False
            self.max_val = node.val

            right = dfs(node.right)
            return left and right

        self.max_val = float('-inf')
        return dfs(root)

