class Solution:
    def reverse(self, x: int) -> int:
        # digit:   log(10) n
        # string: time O(logn)  space O(logn)
        # no string: time O(logn)  space O(1)
        # x = 0
        # y = 321
        # negative

        carry = 1
        if x < 0:
            x = -x
            carry = -1

        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10

        res = y * carry
        return res if - 2 ** 31 <= res < 2 ** 31 else 0


        