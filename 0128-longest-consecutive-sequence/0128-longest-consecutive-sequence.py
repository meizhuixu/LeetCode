class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 1.deduplicate
        # 2.traversal set: n ,  n - 1 
        # time O(n);  space  O(n)

        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            length, curr = 0, num
            while curr in nums:
                length += 1
                curr += 1
            res = max(res, length)

        return res
                
        