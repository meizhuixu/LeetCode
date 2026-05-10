class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                curr = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j - 1], dp[j])
                prev = curr

        return dp[-1]
        