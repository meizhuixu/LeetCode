# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs
        # leaf:  return None
        # find p/q: return p/q
        # itself is not q/p, receive:
        #    two Nones: return None
        #   1  node: return this node
        #   2 node: return itself
        # time: O(n)
        # space: O(h)  avg logn, worst n

        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None


        