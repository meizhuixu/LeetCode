class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: empty
        # two dicts: dict_t and dict_win
        # s = "ADOBECODEBANC", t = "ABC"
        #                l r
        # dict_t = {'A': 1, 'B': 1, 'C': 1}
        # dict_win = {'A': 1, 'B': 1, , 'C': 1}
        # res = 4
        # time: O(n)
        # space: O(1)

        dict_t = Counter(t)
        dict_win = defaultdict(int)
        count = l = 0
        res = (-1, float('inf')) # left pointer, length

        for r in range(len(s)):
            if s[r] in dict_t:
                dict_win[s[r]] += 1
                if dict_win[s[r]] == dict_t[s[r]]:
                    count += 1

            while count == len(dict_t):
                if r - l + 1 < res[1]:
                    res = (l, r - l + 1)
                if s[l] in dict_t:
                    if dict_win[s[l]] == dict_t[s[l]]:
                        count -= 1
                    dict_win[s[l]] -= 1
                l += 1

        return s[res[0]: res[0] + res[1]] if res[1] != float('inf') else ''


        