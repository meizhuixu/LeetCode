class Solution:
    def countCommas(self, n: int) -> int:
        # 1 - 999     0 
        # 1,000 - 999,999    1 * 999,000
        # 1,000,000 - 999,999,999   2 * 999,000,000
        # 1,000,000,000 - 999,999,999,999  3 * 999,000,000,000

        # n = 1,000,003

        if n < 1000:
            return 0

        comma, start, total = 1, 1000, 0
        while n >= start * 1000:
            total += comma * 999 * (1000 ** comma)  # 999,000
            comma += 1   # 2
            start *= 1000  # 1,000,000

        total += (n - start + 1) * comma
        return total
        