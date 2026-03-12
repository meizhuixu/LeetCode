class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(l, r, path):
            if l == r == n:
                res.append(''.join(path))

            if l < n:
                path.append('(')
                backtracking(l+1, r, path)
                path.pop()
            if r < l:
                path.append(')')
                backtracking(l, r+1, path)
                path.pop()

        backtracking(0, 0, [])
        return res
        