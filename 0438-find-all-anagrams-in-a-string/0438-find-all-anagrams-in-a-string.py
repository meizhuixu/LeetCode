class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need = Counter(p)
        seen = defaultdict(int)
        l = matched = 0
        res = []

        for r in range(len(s)):
            if s[r] in need:
                seen[s[r]] += 1
                if seen[s[r]] == need[s[r]]:
                    matched += 1

            if r - l + 1 > len(p):
                if s[l] in need:
                    if seen[s[l]] == need[s[l]]:
                        matched -= 1
                    seen[s[l]] -= 1
                l += 1

            if matched == len(need):
                res.append(l)

        return res

