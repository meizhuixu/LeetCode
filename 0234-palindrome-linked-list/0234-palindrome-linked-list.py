# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # edge case: 1 node, 2 nodes, 3 nodes
        # find mid point and split
        if not head.next:
            return True

        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head_r = slow.next
        slow.next = None

        # reverse the right half
        prev, curr = head_r, head_r.next
        head_r.next = None
        while prev and curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        # check vals
        p1, p2 = head, prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True





        