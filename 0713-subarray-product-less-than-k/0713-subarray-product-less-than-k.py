class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
            
        res, l, prd = 0, 0, 1

        for r in range(len(nums)):
            prd *= nums[r]
            while prd >= k:
                prd //= nums[l]
                l += 1

            res += r - l + 1

        return res


        