class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_list = [(num, i) for i, num in enumerate(nums)]

        idx_list.sort()
        l, r = 0, len(idx_list) - 1
        while l < r:
            total = idx_list[l][0] + idx_list[r][0]
            if total == target:
                return [idx_list[l][1], idx_list[r][1]]
            elif total > target:
                r -= 1
            else:
                l += 1

        return

        