# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        pq = []
        for i in range(k):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        cur = dummy = ListNode()
        while pq:
            val, i, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))

        return dummy.next
