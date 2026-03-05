class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtracking(idx, path):
            res.append(path[:])

            for i in range(idx, n):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res
        