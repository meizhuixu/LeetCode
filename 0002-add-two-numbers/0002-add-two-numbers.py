# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry= 0
        cur = dummy = ListNode()

        while p1 or p2 or carry:
            count = 0
            if p1:
                count += p1.val
                p1 = p1.next
            if p2:
                count += p2.val
                p2 = p2.next
            count += carry
            carry = count // 10
            count %= 10
            cur.next = ListNode(count)
            cur = cur.next


        return dummy.next





        