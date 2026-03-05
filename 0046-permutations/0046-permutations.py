class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        

        def backtracking(level, path):
            if level == n:
                res.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(level + 1, path)
                path.pop()
                used[i] = False

        backtracking(0, [])
        return res
        