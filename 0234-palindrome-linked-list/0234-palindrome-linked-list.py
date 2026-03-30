# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return nums == nums[::-1]
        