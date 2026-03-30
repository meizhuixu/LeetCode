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
            level = deque()
            for _ in range(length):
                cur = queue.popleft()
                if l_to_r:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(list(level))
            l_to_r = not l_to_r

        return res

        


        