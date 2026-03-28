class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            count, total = 1, 0
            for num in nums:
                total += num
                if total > max_sum:
                    count += 1
                    if count > k:
                        return False

                    total = num
            return True


        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2
            
            if can_split(mid):
                r = mid
            else:
                l = mid + 1

        return l

                
        