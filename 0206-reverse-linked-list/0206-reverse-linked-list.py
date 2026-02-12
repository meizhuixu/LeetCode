# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: head = []

        # head = [2,1,3,4,5]
        #      p  t c 

        dummy = ListNode(next=head)
        curr = head

        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = dummy.next
            dummy.next = temp

        return dummy.next