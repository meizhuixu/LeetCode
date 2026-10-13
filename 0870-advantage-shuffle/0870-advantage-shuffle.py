class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # nums2_sorted = [0, 0, 1, 2, 3]
        # nums1_sorted = [1, 2, 2, 4, 0]
        n = len(nums1)
        nums1.sort()
        nums2_sorted = sorted((val, idx) for idx, val in enumerate(nums2))

        res = [-1] * n
        l, r = 0, n - 1  # nums2_sorted
        for num in nums1:
            if num <= nums2_sorted[l][0]:
                res[nums2_sorted[r][1]] = num
                r -= 1
            else: # advantage
                res[nums2_sorted[l][1]] = num
                l += 1

        return res
            
            
            



        