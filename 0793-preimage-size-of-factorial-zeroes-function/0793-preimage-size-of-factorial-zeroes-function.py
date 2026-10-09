class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # k = 0:  0, 1, 2, 3, 4  
        # k = 1:  5, 6, 7, 8, 9   [5m, 5m+4]
        # k = 2:  10, 11, 12, 13, 14  [5m, 5m+4]
        # k = 3:  15, 16, 17, 18, 19  [5m, 5m+4]
        # k = 4:  20, 21, 22, 23, 24
        # k = 6:  25(5*5), 26, 27, 28, 29

        # k can only be 0 or 5
        # if there's such x makes f(x) == k: return 5
        # else: return 0

        def count_zeroes(x):
            count = 0
            while x > 0:
                count += x // 5
                x //= 5
            return count

        l, r = 0, 5 * k + 1
        while l <= r:
            mid = (l + r) // 2
            zeroes = count_zeroes(mid)
            if zeroes == k:
                return 5
            elif zeroes < k:
                l = mid + 1
            else:
                r = mid - 1

        return 0
         