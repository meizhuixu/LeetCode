class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def backtracking(idx, path):
            res.append(path[:])

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res

        