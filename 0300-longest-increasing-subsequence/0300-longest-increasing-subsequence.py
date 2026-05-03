class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find_insert_index(num):
            l, r = 0, len(dp)
            while l < r:
                mid = (l + r) // 2
                if dp[mid] >= num:
                    r = mid
                else:
                    l = mid + 1

            return l

        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                idx = find_insert_index(nums[i])
                dp[idx] = nums[i]

        return len(dp)
        