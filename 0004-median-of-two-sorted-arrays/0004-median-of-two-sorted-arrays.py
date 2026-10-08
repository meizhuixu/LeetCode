class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # half: (m + n + 1) // 2
        # nums1 = [2]
        # nums2 = []
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = (m + n + 1) // 2  #1
        l, r = 0, m  

        while l <= r:
            i = (l + r) // 2  # 0
            j = half - i  # 1

            nums1_l = nums1[i-1] if i > 0 else -float('inf')  #  -float('inf')
            nums1_r = nums1[i] if i < m else float('inf')   # float('inf')
            nums2_l = nums2[j-1] if j > 0 else -float('inf')   #  2
            nums2_r = nums2[j] if j < n else float('inf')   #  float('inf')


            if nums1_l <= nums2_r and nums2_l <= nums1_r:
                if (m + n) % 2 == 1:
                    return max(nums1_l, nums2_l)
                else:
                    return (max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2

            elif nums1_l > nums2_r:
                r = i - 1
            else:
                l = i + 1

        return