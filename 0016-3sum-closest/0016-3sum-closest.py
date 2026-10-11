class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                elif total < target:
                    j += 1
                else:
                    k -= 1

                if abs(total - target) < abs(res - target):
                    res = total

        return res
        