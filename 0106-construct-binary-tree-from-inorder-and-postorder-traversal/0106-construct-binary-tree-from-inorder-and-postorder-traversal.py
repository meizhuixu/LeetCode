# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # reversed postorder idx: root->right->left
        # inorder: array range

        n = len(postorder)
        self.post_idx = n - 1
        in_idx = {val: idx for idx, val in enumerate(inorder)} # time O(n)

        def dfs(l, r):
            if l > r:
                return

            node_val = postorder[self.post_idx]
            self.post_idx -= 1
            node = TreeNode(node_val)

            node_idx = in_idx[node_val]
            node.right = dfs(node_idx + 1, r)
            node.left = dfs(l, node_idx - 1)
            return node

        return dfs(0, n - 1)

            
        