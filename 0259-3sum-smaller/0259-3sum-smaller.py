class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = j + 1
                while k < n:
                    total = nums[i] + nums[j] + nums[k]
                    if total >= target:
                        break
                    else:
                        res += 1
                        k += 1

        return res
        

        