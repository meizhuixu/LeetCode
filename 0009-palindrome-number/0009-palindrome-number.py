class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = 121
        # original = x
        # res = 0

        # new = 121 % 10 = 1  mod
        # res = res * 10 + new = 1
        # x = 121 // 10 = 12

        # new = 12 % 10 = 2
        # res = res * 10 + new = 12
        # x = 12 // 10 = 1

        # new =1 % 10 = 1
        # res = res * 10 + new = 121
        # x = 1 // 10 = 0   stop

        # x == res
        # time: O(n)
        # space: O(1)

        old = x
        new = 0

        while x > 0:
            carry = x % 10
            new = new * 10 + carry
            x //= 10

        return old == new