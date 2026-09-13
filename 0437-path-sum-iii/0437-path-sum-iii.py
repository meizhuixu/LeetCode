# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # edge case: empty
        hashmap = defaultdict(int) # sum: freq
        hashmap[0] = 1
        self.res = 0

        def backtracking(node, total):
            if not node:
                return

            total += node.val
            self.res += hashmap[total - targetSum]

            hashmap[total] += 1
            backtracking(node.left, total)
            backtracking(node.right, total)
            hashmap[total] -= 1
        
        backtracking(root, 0)
        return self.res
        