class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        
        def backtracking(idx, path):
            if idx == n:
                binary_str = ''.join(path)
                if binary_str not in nums_set:
                    return binary_str
                return

            for i in range(2):
                path.append(str(i))
                res = backtracking(idx + 1, path)
                if res:
                    return res
                path.pop()

        return backtracking(0, [])

        