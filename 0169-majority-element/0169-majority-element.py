class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > n / 2:
                return num

        return

        