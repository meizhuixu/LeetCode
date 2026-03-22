class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        res = 0

        for num in nums:
            cur_sum += num
            res += prefix[cur_sum - k]
            prefix[cur_sum] += 1

        return res



        