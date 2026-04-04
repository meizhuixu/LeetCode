class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for chr in s:
            if stack and stack[-1] == chr:
                stack.pop()
            else:
                stack.append(chr)

        return ''.join(stack)
        