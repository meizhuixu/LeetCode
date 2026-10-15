class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        # stack = []
        # hashmap = {')': '('}

        # time: O(n)
        # space: O(n)

        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for b in s:
            if stack and b in hashmap:
                if stack[-1] != hashmap[b]:
                    return False
                stack.pop()

            else:
                stack.append(b)

        return not stack
            
                

