# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        p1, p2 = l1, l2
        carry = 0

        while p1 or p2 or carry:
            total = carry
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next

            cur.next = ListNode(total % 10)
            carry = total // 10
            cur = cur.next

        return dummy.next





        

        