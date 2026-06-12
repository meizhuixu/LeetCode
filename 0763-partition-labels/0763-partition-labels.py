class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s = "eccbbbbdec"
        # start = 0
        # 1: create hashmap 
        # 2: 

        hashmap = {}
        for i, char in enumerate(s):
            hashmap[char] = i

        start = end = 0
        res = []
        for i, char in enumerate(s):
            end = max(end, hashmap[char])
            if i == end:
                res.append(end - start + 1)
                start = end = i + 1

        return res


        