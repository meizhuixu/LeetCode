class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # edge case: empty
        p1 = p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            lo = max(firstList[p1][0], secondList[p2][0])
            hi = min(firstList[p1][1], secondList[p2][1])
            if lo <= hi:
                res.append([lo, hi])

            if firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1

        return res

        