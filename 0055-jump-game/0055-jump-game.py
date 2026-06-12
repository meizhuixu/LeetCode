class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, i, reach = len(nums), 0, 0

        while i <= reach:
            reach = max(reach, i + nums[i])
            if reach >= n - 1:
                return True
            
            i += 1

        return False