class Solution:
    def climbStairs(self, n: int) -> int:
        # dp
        # for n:
        # dp[i] =  dp[i - 1] + dp[i - 2]
        # return dp[-1]
        # dp[1] = 1
        # dp[0] = 1
        # -> dp[2] = 2
        # time: O(n)
        # space: O(1)

        step1 = step2 = cur = 1

        for _ in range(1, n):
            cur = step1 + step2
            step1, step2 = step2, cur

        return cur