class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # n = 3
        # ((())) -> l <= n
        # )  -> r <= l

        res = []

        def backtracking(l, r, path):
            # path store generated paren, array
            # base case
            if l == r == n:
                res.append(''.join(path))
                return

            # add left
            if l < n:
                path.append('(')
                backtracking(l+1, r, path)
                path.pop()

            # add right
            if r < l:
                path.append(')')
                backtracking(l, r+1, path)
                path.pop()

        backtracking(0, 0, [])
        return res




        