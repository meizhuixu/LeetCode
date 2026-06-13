class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        res = curr = nxt = 0
        for i in range(n - 1):
            nxt = max(nxt, i + nums[i])
            if nxt >= n - 1:
                return res + 1
            if i == curr:
                res += 1
                curr = nxt       