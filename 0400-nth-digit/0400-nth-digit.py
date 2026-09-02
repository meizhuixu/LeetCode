class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1-9   9 * 1 = 9
        # 10-99  90 * 2 = 180
        # 100-999 900 * 3 = 2700

        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        target = start + (n - 1) // length
        return int(str(target)[(n - 1) % length])