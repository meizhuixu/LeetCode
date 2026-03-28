class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search
        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2
            count, total = 1, 0
            for num in nums:
                total += num
                if total > mid:
                    count += 1
                    total = num

            if count <= k:
                r = mid
            else:
                l = mid + 1

        return l

                
        