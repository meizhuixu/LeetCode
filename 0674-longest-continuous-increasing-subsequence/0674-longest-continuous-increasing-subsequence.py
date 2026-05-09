class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = prev = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur = prev + 1
                res = max(res, cur)
            else:
                cur = 1
            prev = cur

        return res