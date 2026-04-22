class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        pre1 = cur1 = 0
        for i in range(n - 1):
            temp = cur1
            cur1 = max(nums[i] + pre1, cur1)
            pre1 = temp

        pre2 = cur2 = 0
        for j in range(1, n):
            temp = cur2
            cur2 = max(nums[j] + pre2, cur2)
            pre2 = temp

        return max(cur1, cur2)
        