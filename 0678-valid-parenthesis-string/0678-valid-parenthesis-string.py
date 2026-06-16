class Solution:
    def checkValidString(self, s: str) -> bool:
        # left -> right
        # left: 
        # right -> left
        # right: 

        n = len(s)

        left = 0
        for i in range(n):
            if s[i] == ')':
                left -= 1
            else:
                left += 1

            if left < 0:
                return False

        right = 0
        for j in range(n - 1, -1, -1):
            if s[j] == '(':
                right -= 1
            else:
                right += 1

            if right < 0:
                return False
        
        return True