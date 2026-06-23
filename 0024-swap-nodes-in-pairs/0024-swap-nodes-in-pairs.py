# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: empty
        # recursion
        # head = [1,2,3,4]
        def swapTwo(cur, nxt):
            # base case
            if not nxt:
                return cur

            temp = nxt.next
            nxt.next = cur
            if temp:
                cur.next = swapTwo(temp, temp.next)
            else:
                cur.next = None
            return nxt

        if not head:
            return head

        return swapTwo(head, head.next)
            




        