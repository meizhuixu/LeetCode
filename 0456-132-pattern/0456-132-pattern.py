class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        ak = float('-inf')
        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] < ak:
                return True

            while stack and nums[i] > stack[-1]:
                ak = stack[-1]
                stack.pop()

            stack.append(nums[i])

        return False
        