class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time += (p - 1) // mid + 1

            if time <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l