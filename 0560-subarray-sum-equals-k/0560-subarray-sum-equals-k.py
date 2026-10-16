class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int) # sum: freq
        hashmap[0] = 1
        res = count = 0

        for num in nums:
            count += num
            res += hashmap[count - k]
            hashmap[count] += 1

        return res
            
        