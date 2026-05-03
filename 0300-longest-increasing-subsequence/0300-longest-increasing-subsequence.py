class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find_insert_index(num):
            l, r = 0, len(LIS)
            while l < r:
                mid = (l + r) // 2
                if LIS[mid] >= num:
                    r = mid
                else:
                    l = mid + 1

            return l

        LIS = [nums[0]]
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
                res += 1
            else:
                idx = find_insert_index(nums[i])
                LIS[idx] = nums[i]

        return res
        