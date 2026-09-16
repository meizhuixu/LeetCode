class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)
        y_str = x_str[::-1]

        return x_str == y_str



            

        