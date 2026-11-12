# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        depth_l = 0
        l = root
        while l:
            depth_l += 1
            l = l.left

        depth_r = 0
        r = root
        while r:
            depth_r += 1
            r = r.right

        if depth_l == depth_r:
            return 2 ** depth_l - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)





        

        