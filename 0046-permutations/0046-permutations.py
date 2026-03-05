class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtracking(level, path):
            if level == n:
                res.append(path[:])
                return

            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtracking(level + 1, path)
                path.pop()

        backtracking(0, [])
        return res
        