class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix
        n = len(nums)
        prefix = [1] * n

        pre = 1
        for i in range(n):
            prefix[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1):
            prefix[i] *= post
            post *= nums[i]

        return prefix

        