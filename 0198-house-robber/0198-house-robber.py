class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        m1, m2 = 0, nums[0]
        for i in range(1, n):
            cur = max(m1 + nums[i], m2)
            m1, m2 = m2, cur

        return cur