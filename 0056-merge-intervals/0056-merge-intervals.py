class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = []
        last = -1
        for s, e in intervals:
            if s > last:
                res.append([s, e])
                last = e
            else:
                res[-1][1] = max(res[-1][1], e)
                last = res[-1][1]

        return res


        