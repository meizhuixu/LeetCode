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

            if not dfs(node.left):
                return False
                
            if node.val <= self.max_val:
                return False
            else:
                self.max_val = node.val
                return dfs(node.right)

        self.max_val = float('-inf')
        return dfs(root)

