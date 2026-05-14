# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # edge case: empty tree
        res = []
        if not root:
            return res
        
        def dfs(node, path, total):
            if total == targetSum and not node.left and not node.right:
                res.append(path[:])
                return


            if node.left:
                path.append(node.left.val)
                dfs(node.left, path, total + node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, path, total + node.right.val)
                path.pop()

        dfs(root, [root.val], root.val)
        return res