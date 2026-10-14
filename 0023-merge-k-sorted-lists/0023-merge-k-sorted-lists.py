# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # edge case: empty lists, empty list
        pq = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))

        curr = dummy = ListNode()
        while pq:
            _, idx, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))

        return dummy.next



        