# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # lists = [[1,4,5],[1,3,4],[2,6]]
        # pq = [    ]
        # res = [1, 1, 2, 3, 4, 4, 5, 6]
        # (node.val, i, node)
        # time: O(nlogk)
        # k = number of linked-lists
        # n = number of nodes
        # space: O(k)

        pq = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))

        cur = dummy = ListNode()
        while pq:
            val, idx, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))

        return dummy.next

        

        