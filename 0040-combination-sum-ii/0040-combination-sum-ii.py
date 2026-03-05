class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtracking(idx, path, total):
            if total == target:
                res.append(path[:])
            if total >= target:
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtracking(i + 1, path, total + candidates[i])
                path.pop()

        backtracking(0, [], 0)
        return res