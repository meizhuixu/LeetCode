class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def searchfirst(target):
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        first = searchfirst(target)
        last = searchfirst(target + 1) - 1
        if first == n or nums[first] != target:
            return [-1, -1]
        return [first, last]
