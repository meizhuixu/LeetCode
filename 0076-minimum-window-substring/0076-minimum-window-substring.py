class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = (-1, float('inf'))
        l = match = 0
        need = Counter(t)
        window = defaultdict(int)
        
        for r in range(len(s)):
            if s[r] in need:
                window[s[r]] += 1
                if window[s[r]] == need[s[r]]:
                    match += 1

            while match == len(need):
                if r - l + 1 < res[1]:
                    res = (l, r - l + 1)
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1

        return s[res[0]: res[0] + res[1]] if res[0] != -1 else ''


            

        