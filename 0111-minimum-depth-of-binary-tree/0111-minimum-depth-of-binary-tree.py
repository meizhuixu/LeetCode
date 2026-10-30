# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        # no childre(leaf) -> return 1
        # two non empty children -> min
        # one empty -> return the non-empty one

        # time: O(n)
        # space: dfs O(h)   logn -  n

        # edge case: empty root
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left and root.right:
            return min(left, right) + 1
        elif not root.left:
            return right + 1
        else:
            return left + 1
        