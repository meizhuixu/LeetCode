# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val < p2.val:
                cur.next = ListNode(p1.val)
                p1 = p1.next
            else:
                cur.next = ListNode(p2.val)
                p2 = p2.next
            cur = cur.next

        if p1:
            cur.next = p1
        else:
            cur.next = p2

        return dummy.next

        