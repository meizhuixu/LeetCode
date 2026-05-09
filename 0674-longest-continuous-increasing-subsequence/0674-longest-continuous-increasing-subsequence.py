class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = length = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                length += 1
                res = max(res, length)
            else:
                length = 1

        return res