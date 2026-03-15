class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = (m + n + 1) // 2
        l, r = 0, m # left and right means how many numbers, instead of index
        while l <= r:
            i = (l + r) // 2
            j = half - i

            nums1_l = nums1[i - 1] if i > 0 else float('-inf')
            nums1_r = nums1[i] if i < m else float('inf')
            nums2_l = nums2[j - 1] if j > 0 else float('-inf')
            nums2_r = nums2[j] if j < n else float('inf')

            if nums1_l <= nums2_r and nums1_r >= nums2_l:
                if (m + n) % 2 == 1:
                    return max(nums1_l, nums2_l)
                else:
                    return (max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2 # single dimension

            elif nums1_l > nums2_r:
                r = i - 1
            else:
                l = i + 1

        return


        