class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        n = len(s)

        for i in range(n):
            cur_val = hashmap[s[i]]
            if i < n - 1 and cur_val < hashmap[s[i + 1]]:
                res -= cur_val
            else:
                res += cur_val

        return res