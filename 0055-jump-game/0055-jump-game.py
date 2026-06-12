class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, reach = len(nums), 0

        for i in range(n):
            reach = max(reach, i + nums[i])
            if reach >= n - 1:
                return True
            if reach <= i:
                return False

        return
        