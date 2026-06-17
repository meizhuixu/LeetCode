class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        # fruits = [1,2,3,2,2]
        # kind 2   dict  kind: freq
        # length 2
        # res max length

        l = res = 0
        hashmap = {}

        for r in range(len(fruits)):
            curr = fruits[r]
            if curr in hashmap:
                hashmap[curr] += 1
            else:
                hashmap[curr] = 1
            
            while len(hashmap) > 2:
                drop = fruits[l]
                hashmap[drop] -= 1
                if hashmap[drop] == 0:
                    del hashmap[drop]
                l += 1

            res = max(res, r - l + 1)

        return res


        