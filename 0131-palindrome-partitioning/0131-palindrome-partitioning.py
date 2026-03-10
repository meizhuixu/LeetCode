class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def is_palindrome(s):
            m = len(s)
            l, r = 0, m - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtracking(idx, path):
            if idx == n:
                res.append(path[:])
                return 

            for i in range(idx, n):
                substr = s[idx: i + 1]
                if is_palindrome(substr):
                    path.append(substr)
                    backtracking(i + 1, path)
                    path.pop()

        backtracking(0, [])
        return res


            
        