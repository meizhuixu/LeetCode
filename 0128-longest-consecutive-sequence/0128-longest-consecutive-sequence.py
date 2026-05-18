class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set
        # num : num - 1  start of consecutive sequence -> num + 1  ... the length
        # time: O(n) worst
        # 1, 2, 3, 4  O(2n)
        # space: O(n)

        # edge case: empty
        res = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue

            length = 0
            while num in nums:
                length += 1
                num += 1
            res = max(res, length)

        return res
                
        