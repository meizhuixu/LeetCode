class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        s1 = s2 = 1
        result = 0
        for _ in range(2, n + 1):
            result = s1 + s2
            s1 = s2
            s2 = result

        return result


        