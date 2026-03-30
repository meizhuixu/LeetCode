class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0

        for num in nums:
            temp = cur
            cur = max(num + pre, cur)
            pre = temp

        return cur
        