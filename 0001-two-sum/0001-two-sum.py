class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i, num in enumerate(nums):
            if num in hashmap:
                return [i, hashmap[num]]
            hashmap[target - num] = i

        return

        