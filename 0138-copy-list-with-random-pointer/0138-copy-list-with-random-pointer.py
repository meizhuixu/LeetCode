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
        if not head:
            return None
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
        new_head = head.next
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1.next = p2.next
            p2.next = p2.next.next
            p1, p2 = p1.next, p2.next
        return new_head
        