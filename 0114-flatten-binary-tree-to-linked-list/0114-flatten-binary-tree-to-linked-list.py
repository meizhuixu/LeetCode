# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
          1
           \   
            2     
             \
              3

        """
        # iteration : space O(1)
        # time: O(n)

        # step1 : move right subtree to the most right node of left subtree
        # step2: move left subtree to right subtree
        # step3: move to next node

        # edge case: empty
        curr = root
        while curr:
            if curr.left:
                right_subtree = curr.right
                # find most right of left subtree
                most_right = curr.left
                while most_right.right:
                    most_right = most_right.right
                # move right subtree to most right
                most_right.right = right_subtree

                # move left subtree to right
                curr.right = curr.left
                curr.left = None
                
            curr = curr.right


        