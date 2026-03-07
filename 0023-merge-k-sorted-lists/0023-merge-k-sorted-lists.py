# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initialize an empty list pq as my heap
        pq = []
        # iterate through the initial $k$ lists
        for i, node in enumerate(lists):
            # push the head of each non-empty list into the heap
            if node:
                # The i (index) acts as a tie-breaker to prevent the heap from comparing the ListNode objects directly if their values are identical
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        cur = dummy = ListNode()
        # while the heap is not empty
        while pq:
            # repeatedly pop the smallest element
            _, i, node = heapq.heappop(pq)
            # connect this node to my dummy result
            cur.next = node
            # move the cur pointer forward
            cur = cur.next

            # if the popped node has a next element (node.next)
            if node.next:
                # push that next node into the heap
                # This ensures the heap always contains the next candidate from each list, maintaining a constant size of at most $k$.
                heapq.heappush(pq, (node.next.val, i, node.next))

        return dummy.next
