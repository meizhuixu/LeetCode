class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = n - 2
        
        # 1. Find the first element from the right that breaks the descending order
        while p1 >= 0 and nums[p1] >= nums[p1 + 1]:
            p1 -= 1  # p1 is the index of the element to be swapped
            
        # 2. Find the first element from the right that is strictly greater than nums[p1] and swap them
        if p1 >= 0:
            p2 = n - 1
            while nums[p2] <= nums[p1]:
                p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
            
        # 3. Reverse the suffix after p1 to convert it from descending to ascending order
        l, r = p1 + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1