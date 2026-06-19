class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2]
        #  l           r
        # [0,1,2,4,5,6,7]
        #  l           r
        # binary search
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:   # 0, 1
            mid = (l + r) // 2   # 0
            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


        