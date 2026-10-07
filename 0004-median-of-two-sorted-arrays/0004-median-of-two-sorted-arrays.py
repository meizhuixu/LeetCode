class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = (m + n) // 2
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = half - i
            if i > 0 and j < n and nums1[i-1] > nums2[j]:
                r = i - 1
            elif j > 0 and i < m and nums2[j-1] > nums1[i]:
                l = i + 1
            else:
                break

        if i == m:
            min_right = nums2[j]
        elif j == n:
            min_right = nums1[i]
        else:
            min_right = min(nums1[i], nums2[j])

        if i == 0:
            max_left = nums2[j-1]
        elif j == 0:
            max_left = nums1[i-1]
        else:
            max_left = max(nums1[i-1], nums2[j-1])
        return (max_left + min_right) / 2 if (m + n) % 2 == 0 else min_right
        