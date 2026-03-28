class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen_pos = set()

        for num in nums:
            if num > 0:
                seen_pos.add(num)

        for i in range(1, len(nums) + 2):
            if i not in seen_pos:
                return i

                

        