class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # a, b, c -> target
        # [False, False, False]
        x, y, z = target
        res = [False, False, False]

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            if a == x:
                res[0] = True
            if b == y:
                res[1] = True
            if c == z:
                res[2] = True

        return all(res)




        