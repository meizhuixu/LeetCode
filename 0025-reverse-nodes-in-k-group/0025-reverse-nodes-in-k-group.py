# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
            
        # get the length of linked list
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
            
        # reverse k nodes
        dummy = ListNode(next=head)
        cur, prev = head, dummy
        for _ in range(length // k):
            for _ in range(k - 1):
                # [dummy,|  1,  2, 3,| 4, 5, 6,| 7] k = 3
                #    prev      cur temp
                temp = cur.next
                cur.next = temp.next
                temp.next = prev.next
                prev.next = temp
            prev = cur
            cur = cur.next
            
        return dummy.next