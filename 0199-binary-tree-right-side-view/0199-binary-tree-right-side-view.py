# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                if i == 0:
                    res.append(cur.val)
                
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)

        return res


        