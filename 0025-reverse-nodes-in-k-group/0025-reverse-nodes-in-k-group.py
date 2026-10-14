# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # edge case: k = 1, n = 1
        if k == 1:
            return head

        # count length
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        prev = dummy = ListNode(next=head)
        curr = head
        for _ in range(length // k):
            for _ in range(k - 1):
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            prev = curr
            curr = curr.next

        return dummy.next
        