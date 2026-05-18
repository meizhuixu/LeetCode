class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1

            res = max(res, count)

        return res


        