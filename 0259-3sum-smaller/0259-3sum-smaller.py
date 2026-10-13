class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if  total < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1

        return res