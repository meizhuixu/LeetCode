class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 = [1,3], nums2 = []
        # nums1 = [], nums2 = [2]
        # nums1 = [], nums2 = []

        # half: number <= median
        # binary search [mid]
        # nums1: i numbers    |  bigger
        # nums2: j = half - i | bigger
        # 1. m + n: odd
        # max()
        # 2. m + n: even
        # average(max(), max())

        # time: O(logm)  m = len(nums1)
        # space: O(1)

        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = (m + n + 1) // 2
        l, r = 0, m # how much numbers in the left part, instead of index
        while l <= r:
            i = (l + r) // 2
            j = half - i

            # nums1: ... nums1[i-1] | nums1[i]
            # nums2: ... nums2[j-1] | nums2[j]

            if i > 0 and j < n and nums1[i - 1] > nums2[j]:
                r = i - 1
            elif j > 0 and i < m and nums2[j - 1] > nums1[i]:
                l = i + 1
            else:
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return left_max
                else:
                    if i == m:
                        right_min = nums2[j]
                    elif j == n:
                        right_min = nums1[i]
                    else:
                        right_min = min(nums1[i], nums2[j])

                    return (left_max + right_min) / 2