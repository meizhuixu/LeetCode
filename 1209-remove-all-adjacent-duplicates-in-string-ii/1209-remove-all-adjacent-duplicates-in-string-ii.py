class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for chr in s:
            if stack and chr == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([chr, 1])

        res = []
        for chr, freq in stack:
            res.append(chr * freq)
        return ''.join(res)
