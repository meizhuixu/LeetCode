# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        # postorder
        # dict = {[vals]: [treenodes]}

        self.hashmap = defaultdict(list)
        self.res = []

        def postorder(node):
            if not node:
                return [None]

            vals = []
            vals.extend(postorder(node.left))
            vals.extend(postorder(node.right))
            vals.append(node.val)

            if len(self.hashmap[tuple(vals)]) == 1:
                self.res.append(node)

            self.hashmap[tuple(vals)].append(node)
            return vals

        postorder(root)
        return self.res



        