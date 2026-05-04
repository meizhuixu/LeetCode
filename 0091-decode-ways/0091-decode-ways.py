class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        p1 = p2 = 1
        for i in range(len(s)):
            total = 0
            if int(s[i]) > 0:
                total += p2
            if i > 0 and 10 <= int(s[i - 1: i + 1]) <= 26:
                total += p1
            p1, p2 = p2, total

        return total