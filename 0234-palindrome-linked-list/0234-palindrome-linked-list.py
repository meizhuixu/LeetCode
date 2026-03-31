# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find cut point
        slow = fast = dummy = ListNode(next = head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the right half
        if slow.next and slow.next.next:
            pre, cur, nxt = slow, slow.next.next, slow.next
            nxt.next = None
            while cur:
                temp = cur.next
                pre.next = cur
                cur.next = nxt
                cur, nxt = temp, cur

        p1, p2 = head, slow.next
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1, p2 = p1.next, p2.next

        return True

        
        