# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:

        def serialize(node):
            if not node:
                return '#'

            subtree = f'{node.val},{serialize(node.left)},{serialize(node.right)}'
            self.hashmap[subtree] += 1
            if self.hashmap[subtree] == 2:
                self.res.append(node)
            
            return subtree

        self.hashmap = defaultdict(int)
        self.res = []
        serialize(root)

        return self.res



