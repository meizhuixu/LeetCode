# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {num: i for i, num in enumerate(inorder)}
        self.count = 0

        def dfs(l, r):
            if l > r:
                return
                
            val = preorder[self.count]
            node = TreeNode(val)
            self.count += 1

            inorder_idx = hashmap[val]
            node.left = dfs(l, inorder_idx - 1)
            node.right = dfs(inorder_idx + 1, r)

            return node

        return dfs(0, len(preorder) - 1)
        