class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ''

        need = Counter(t)
        target = len(need)
        window = defaultdict(int)
        l = matched = 0
        res = (-1, float('inf')) # start, length

        for r in range(len(s)):
            if s[r] in need:
                window[s[r]] += 1
                if window[s[r]] == need[s[r]]:
                    matched += 1

            while matched == target:
                if r - l + 1 < res[1]:
                    res = (l, r - l + 1)
                if s[l] in need:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        matched -= 1
                l += 1

        return s[res[0]: res[0] + res[1]] if res[1] != float('inf') else ''


        