class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two array: prefix and suffix
        # prefix[i]: product of numbers before nums[i]
        # suffix[i]: product of numbers after nums[i]
        # res[i] = prefix[i] * suffix[i]
        # time: O(n)
        # space: O(n)

        # res[i]
        # 1. prefix: left -> right
        # 2. res[i] * suffix : right -> left
        # space: O(1)

        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):
            res[i] *= pre
            pre *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res

        