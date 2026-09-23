class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # generate
        # left: left <= n
        # right: right <= left
        # backtracking
        
        # time O(2^n)   space  O(n)
        
        def backtracking(path, left, right):
            if left == right == n:
                res.append(''.join(path))
                return
                
            if left < n:
                path.append('(')
                backtracking(path, left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                backtracking(path, left, right + 1)
                path.pop()
            
        res = []
        backtracking([], 0, 0)
        
        return res
        