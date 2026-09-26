class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # sliding window
        # [10, 50, 100, 600]
        # time O(n*n)  space O(n)
        # nums = [10,5,2,6]
        l = r = 0
        res = 0
        product = 1
        
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product //= nums[l]
                l += 1

            res += r - l + 1

        return res

        






        