class Solution:
    def findMin(self, nums: List[int]) -> int:
        # edge case: [1, 2, 3, 4]
        # binary search 
        # mid & right
        # mid < right: right part, search left
        # mid > right: left part, search right
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[-1]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return nums[res]
        

        