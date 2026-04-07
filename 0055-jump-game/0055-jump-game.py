class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = i = 0
        n = len(nums)

        while reach >= i:
            reach = max(reach, i + nums[i])
            if reach >= n - 1:
                return True
            i += 1

        return False
        