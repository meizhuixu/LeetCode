class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = res = 0
        hashmap = defaultdict(int)

        for i, char in enumerate(s):
            hashmap[char] += 1
            while hashmap[char] > 1:
                hashmap[s[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res