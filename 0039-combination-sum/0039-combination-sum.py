class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if target == 1:
            return res
        n = len(candidates)

        def backtracking(idx, path, total):
            if total == target:
                res.append(path[:])
            if total >= target:
                return

            for i in range(idx, n):
                path.append(candidates[i])
                backtracking(i, path, total + candidates[i])
                path.pop()

        backtracking(0, [], 0)
        return res
        