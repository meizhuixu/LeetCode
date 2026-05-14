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
            if node:
                path.append(node.val)
                total += node.val
                if total == targetSum and not node.left and not node.right:
                    res.append(path[:])
                else:
                    dfs(node.left, path, total)
                    dfs(node.right, path, total)
                path.pop()
                total -= node.val

        dfs(root, [], 0)
        return res