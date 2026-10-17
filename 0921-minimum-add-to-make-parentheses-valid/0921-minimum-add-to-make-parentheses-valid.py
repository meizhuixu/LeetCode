class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        res = 0
        for chr in s:
            if chr == ')':
                if stack:
                    stack.pop()
                else:
                    res += 1
            else:
                stack.append(chr)

        return res + len(stack)
        