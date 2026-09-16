class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = res = 0
        seen = set()

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            res = max(res, r - l + 1)

        return res