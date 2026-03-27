class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            count_hour = 0
            for p in piles:
                count_hour += (p + mid - 1) // mid

            if count_hour > h:
                l = mid + 1
            else:
                r = mid

        return l

         