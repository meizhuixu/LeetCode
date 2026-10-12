class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers
        if val > 50:
            return len(nums)

        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
