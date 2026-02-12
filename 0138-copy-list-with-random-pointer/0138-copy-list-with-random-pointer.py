"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy and insert after the original node
        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = copy.next

        # copy random
        cur = head
        while cur and cur.next:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next

        # split into two linked lists
        dummy = Node(0)
        p1, p2 = dummy, head
        while p2:
            p1.next = p2.next
            p1, p2 = p1.next, p1.next.next
            
        return dummy.next
        