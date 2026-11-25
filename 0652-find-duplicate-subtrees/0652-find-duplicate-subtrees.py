# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:

        def traverse(node):
            if not node:
                return 0

            subtree = (node.val, traverse(node.left), traverse(node.right))
            if subtree not in tree_to_id:
                tree_to_id[subtree] = len(tree_to_id) + 1
            sub_id = tree_to_id[subtree]

            count[sub_id] += 1
            if count[sub_id] == 2:
                res.append(node)
            
            return sub_id

        count = defaultdict(int)
        tree_to_id = {}
        res = []
        traverse(root)

        return res



