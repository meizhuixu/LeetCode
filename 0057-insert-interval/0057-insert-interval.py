class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        s, e = newInterval

        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        
        while i < n and intervals[i][0] <= e:
            s = min(intervals[i][0], s)
            e = max(intervals[i][1], e)
            i += 1
        res.append([s, e])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        








        