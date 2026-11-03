# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

        # dfs(l, r) inorder
        # preorder is the order of root, recursion one by one
        # time O(n)
        # space O(h)

        self.idx = 0 # idx of preorder, represent the root of this subtree
        self.val_to_idx = {val: idx for idx, val in enumerate(inorder)}

        def dfs(l, r):  # boundary in inorder array
            if l > r:
                return
            node_val = preorder[self.idx]
            self.idx += 1
            node = TreeNode(node_val)
            node_inorder_idx = self.val_to_idx[node_val]

            node.left = dfs(l, node_inorder_idx - 1)
            node.right = dfs(node_inorder_idx + 1, r)

            return node

        return dfs(0, len(preorder) - 1)


        