class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # edge case: empty nums;  not found
        if not nums:
            return [-1, -1]

        def searchInsertPosition(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        first = searchInsertPosition(nums, target)
        if first >= len(nums) or nums[first] != target:  # if not found (first == len(nums))
            return [-1, -1]

        last = searchInsertPosition(nums, target + 1) - 1  # must found
        return [first, last] 



        