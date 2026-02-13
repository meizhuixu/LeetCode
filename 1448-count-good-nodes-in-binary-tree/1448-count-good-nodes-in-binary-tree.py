# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def ifGood(max_val, node):
            if not node:
                return

            if node.val >= max_val:
                self.count += 1
                max_val = node.val

            ifGood(max_val, node.left)
            ifGood(max_val, node.right)

        ifGood(float('-inf'), root)
        return self.count


        