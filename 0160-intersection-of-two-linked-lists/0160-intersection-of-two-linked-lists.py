# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # edge case: no intersection
        p1, p2 = headA, headB
        while p1 != p2:
            if not p1 and not p2:
                return None
            elif not p1:
                p1 = headB
            elif not p2:
                p2 = headA
            else:
                p1 = p1.next
                p2 = p2.next
        
        return p1

  