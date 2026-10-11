class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = fast = 0
        n = len(nums)
        for fast in range(n):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]

        return slow + 1
                


        