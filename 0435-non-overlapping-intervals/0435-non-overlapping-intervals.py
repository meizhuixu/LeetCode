class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = intervals[0][1]
        res = 0
        

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < last:
                res += 1
                last = min(last, e)
            else:
                last = e

        return res