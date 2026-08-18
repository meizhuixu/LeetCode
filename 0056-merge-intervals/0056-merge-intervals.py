class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time: O(nlogn); space: O(n)
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last_end = res[-1][1]
            s, e = intervals[i]
            if s > last_end:
                res.append([s, e])
            else:
                res[-1][1] = max(e, last_end)

        return res
