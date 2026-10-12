class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers
        if val > 50:
            return len(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1

        return l