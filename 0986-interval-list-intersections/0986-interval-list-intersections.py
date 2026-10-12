class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # edge case: empty
        p1 = p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            s1, e1 = firstList[p1][0], firstList[p1][1]
            s2, e2 = secondList[p2][0], secondList[p2][1]
            if e1 < s2:
                p1 += 1
            elif e2 < s1:
                p2 += 1
            else:
                res.append([max(s1, s2), min(e1, e2)])
                if e1 > e2:
                    p2 += 1
                else:
                    p1 += 1

        return res

        