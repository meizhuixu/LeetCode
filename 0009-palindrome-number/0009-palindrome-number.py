class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x < 0: return False
        # x >= 0: two pointers
        # int -> str, l and r from left and right
        # if l == r , move inwards
        # if l != r: return False
        # time: O(n) n= len(str(s))
        # space: O(1)

        if x < 0:
            return False

        s = str(x)
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
        