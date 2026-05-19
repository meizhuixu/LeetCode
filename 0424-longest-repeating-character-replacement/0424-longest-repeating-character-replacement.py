class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # time: O(n)
        # space: O(1)   26
        # s = "AABABBA", k = 1
        #          l r
        # hashmap = {'A': 1, 'B': 2 }
        # res = 4

        # "BAAAB"  k = 2
        # hashmap = {'A':3 , 'B': 2 }

        hashmap = defaultdict(int)
        res = l = count = 0

        for r in range(len(s)):
            char = s[r]
            hashmap[char] += 1
            count = max(count, hashmap[char])
            while r - l + 1 - count > k:
                drop = s[l]
                hashmap[drop] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
        