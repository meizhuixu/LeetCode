class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = length = 0
        for c in s:   # can count '())', can't count '(()'
            if c == '(':
                left += 1
            else:
                right += 1

            if right == left:
                length = max(length, right * 2)
            elif right > left:
                left = right = 0

        left = right = 0
        for c in reversed(s):  # can count '(()', can't count '())'
            if c == '(':
                left += 1
            else:
                right += 1

            if right == left:
                length = max(length, right * 2)
            elif left > right:
                left = right = 0

        return length