class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = most = 0
        seen = defaultdict(int)

        for r in range(len(s)):
            seen[s[r]] += 1
            most = max(most, seen[s[r]])
            
            if (r - l + 1) - most > k:
                seen[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        