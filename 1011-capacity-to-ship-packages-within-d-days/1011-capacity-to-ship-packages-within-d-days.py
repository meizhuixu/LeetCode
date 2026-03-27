class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2

            count_days = 1
            count_weight = 0
            for w in weights:
                count_weight += w
                if count_weight > mid:
                    count_days += 1
                    count_weight = w

            if count_days > days:
                l = mid + 1
            else:
                r = mid

        return l

            




        