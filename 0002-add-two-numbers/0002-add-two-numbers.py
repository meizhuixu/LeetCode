# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        p1, p2 = l1, l2
        carry = 0
        dummy = curr = ListNode()

        while p1 or p2 or carry:
            if p1:
                carry += p1.val
                p1 = p1.next
            if p2:
                carry += p2.val
                p2 = p2.next

            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10

        return dummy.next
            



        