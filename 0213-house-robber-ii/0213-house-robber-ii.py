class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        pre = cur1 = 0
        for i in range(n - 1):
            temp = cur1
            cur1 = max(nums[i] + pre, cur1)
            pre = temp

        pre = cur2 = 0
        for i in range(1, n):
            temp = cur2
            cur2 = max(nums[i] + pre, cur2)
            pre = temp

        return max(cur1, cur2)

        
        