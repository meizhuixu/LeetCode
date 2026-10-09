class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2
            count_days, count_weight = 1, 0 
            for w in weights:
                if count_weight + w > mid:
                    count_weight = 0
                    count_days += 1
                count_weight += w

            if count_days <= days:
                r = mid - 1
            else:
                l = mid + 1

        return l
        