# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # edge case: empty list
        p = ListNode(-101, head)
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head


        