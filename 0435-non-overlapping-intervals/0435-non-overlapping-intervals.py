class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        remove = 0
        last_end = float('-inf')
        for s, e in intervals:
            if s >= last_end:
                last_end = e
            else:
                last_end = min(last_end, e)
                remove += 1

        return remove
        