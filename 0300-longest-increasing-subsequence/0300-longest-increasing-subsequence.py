class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp O(n*n)
        # O(nlogn)
        # nums = [10,9,2,5,3,7,101,18]
        # res = [2, 3, 7, 18]
        res = []
        for num in nums:
            insert = bisect.bisect_left(res, num)
            if insert == len(res):
                res.append(num)
            else:
                res[insert] = num

        return len(res)

        