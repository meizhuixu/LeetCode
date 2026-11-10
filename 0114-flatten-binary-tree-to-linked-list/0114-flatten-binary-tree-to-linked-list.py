# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        vals = []
        def dfs(node):
            if not node:
                return

            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        curr = root
        for i in range(1, len(vals)):
            curr.left = None
            curr.right = TreeNode(vals[i])
            curr = curr.right
