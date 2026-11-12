"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # empty root
        if not root or not root.left:
            return root

        most_left = root
        while most_left.left:
            curr = most_left

            while curr:  # 3
                curr.left.next = curr.right   # 4->5   6->7

                if curr.next:    # 3
                    curr.right.next = curr.next.left  # 5->6
                curr = curr.next  # 

            most_left = most_left.left

        return root

        

        