class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = -1
        l, r = 0, len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]
            if total < k:
                res = max(res, total)
                l += 1
            else:
                r -= 1

        return res