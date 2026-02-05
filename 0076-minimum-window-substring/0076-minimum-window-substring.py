class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        dict_t = Counter(t)
        need = len(dict_t)

        dict_win = defaultdict(int)
        l = meet = 0
        res = (0, float('inf'))

        for r in range(len(s)):
            cur = s[r]
            dict_win[cur] += 1
            if dict_win[cur] == dict_t[cur]:
                meet += 1

            while meet == need:
                if r - l + 1 < res[1]:
                    res = (l, r - l + 1)

                drop = s[l]
                if dict_win[drop] == dict_t[drop]:
                    meet -= 1
                dict_win[drop] -= 1
                l += 1

        return '' if res[1] == float('inf') else s[res[0]: res[0] + res[1]]


        