class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        unique = [num for num in hashmap.keys()]

        def partition(l, r):
            pivot_idx = random.randint(l, r)
            pivot_freq = hashmap[unique[pivot_idx]]
            unique[pivot_idx], unique[r] = unique[r], unique[pivot_idx]

            store = l
            for i in range(l, r):
                if hashmap[unique[i]] < pivot_freq:
                    unique[i], unique[store] = unique[store], unique[i]
                    store += 1
                
            unique[store], unique[r] = unique[r], unique[store]
            return store

        n = len(unique)
        l, r = 0, n - 1

        while l <= r:
            p = partition(l, r)
            if p == n - k:
                return unique[p:]
            elif p < n - k:
                l = p + 1
            else:
                r = p - 1

