class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist(p):
            return p[0] * p[0] + p[1] * p[1]

        def partition(l, r):
            pivot_idx = random.randint(l, r)
            pivot_dist = dist(points[pivot_idx])
            points[pivot_idx], points[r] = points[r], points[pivot_idx]

            i = l
            for j in range(l, r):
                if dist(points[j]) <= pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[i], points[r] = points[r], points[i]
            return i

        l, r = 0, len(points) - 1
        while l <= r:
            p = partition(l, r)
            if p == k:
                break
            elif p > k - 1:
                r = p - 1
            else:
                l = p + 1

        return points[:k]
