# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        l_to_r = True
        while queue:
            
            length = len(queue)
            level = []
            for _ in range(length):
                cur = queue.popleft()
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if not l_to_r:
                level.reverse()
            res.append(level)
            l_to_r = not l_to_r

        return res

        


        