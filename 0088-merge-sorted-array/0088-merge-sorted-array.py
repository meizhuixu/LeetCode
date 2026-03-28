class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        for p in range(m + n - 1, -1, -1):
            if j < 0:
                break
            elif i >= 0 and nums1[i] > nums2[j]:
                nums1[i], nums1[p] = nums1[p], nums1[i]
                i -= 1
            else:
                nums2[j], nums1[p] = nums1[p], nums2[j]
                j -= 1
