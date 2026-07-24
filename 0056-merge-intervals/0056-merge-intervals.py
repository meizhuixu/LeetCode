class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        for s, e in intervals:
            hashmap[s] += 1
            hashmap[e] -= 1

        count = 0
        res = []
        pair = []
        for i in sorted(hashmap.keys()):
            if not pair:
                pair.append(i)

            count += hashmap[i]
            if count == 0:
                pair.append(i)
                res.append(pair)
                pair = []

        return res



        

        