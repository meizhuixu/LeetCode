class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        need = Counter(s1)
        seen = defaultdict(int)
        l = matched = 0

        for r in range(n):
            if s2[r] in need:
                seen[s2[r]] += 1
                if seen[s2[r]] == need[s2[r]]:
                    matched += 1

            if r - l + 1 > len(s1):
                if s2[l] in need:
                    if seen[s2[l]] == need[s2[l]]:
                        matched -= 1
                    seen[s2[l]] -= 1
                l += 1

            if matched == len(need):
                return True

        return False
        