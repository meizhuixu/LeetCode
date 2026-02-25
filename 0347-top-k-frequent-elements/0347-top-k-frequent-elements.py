class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)

        n = len(nums)
        bucket = [[] for i in range(n + 1)]
        for num, freq in hashmap.items():
            bucket[freq].append(num)

        res = []
        count = 0
        for freq in range(n, 0, -1):
            for f in bucket[freq]:
                res.append(f)
                count += 1
                if count == k:
                    return res


        