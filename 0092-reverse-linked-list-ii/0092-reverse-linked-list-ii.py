# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # edge case: left = right, left = 1
        dummy = ListNode(next=head)

        # find prev
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # reverse
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next
        