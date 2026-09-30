class Solution:
    def countCommas(self, n: int) -> int:
        # 1 - 999     0 
        # 1,000 - 999,999    1 * 999,000
        # 1,000,000 - 999,999,999   2 * 999,000,000
        # 1,000,000,000 - 999,999,999,999  3 * 999,000,000,000

        # n = 1,000,003

        start, total = 1000, 0

        while start <= n:
            total += n - start + 1
            start *= 1000

        return total
