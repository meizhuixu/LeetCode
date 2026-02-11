# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        pre = dummy = ListNode(next=head)
        cur = head
        for _ in range(length // k):
            for _ in range(k - 1):
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            pre = cur
            cur = cur.next

        return dummy.next
        