class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        seen = set()

        for r, chr in enumerate(s):
            while chr in seen:
                seen.remove(s[l])
                l += 1
            seen.add(chr)
            res = max(res, r - l + 1)

        return res



        