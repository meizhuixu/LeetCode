# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid and divide into 2 linked lists
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None

        # reverse the second linked list
        prev, cur = None, new_head
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        # head of reversed linked list is prev

        # merge two linked lists into one
        p1, p2 = head, prev
        while p1 and p2:
            temp = p2.next
            p2.next = p1.next
            p1.next = p2
            p1, p2 = p2.next, temp

            

        





        