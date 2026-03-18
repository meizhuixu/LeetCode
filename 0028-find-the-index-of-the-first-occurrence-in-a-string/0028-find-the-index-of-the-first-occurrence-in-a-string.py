class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        next = [0] * m

        j = 0
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]:
                j = next[j - 1]
            if needle[j] == needle[i]:
                j += 1
            next[i] = j

        j = 0
        for i in range(n):
            while j > 0 and needle[j] != haystack[i]:
                j = next[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == m:
                return i - j + 1

        return -1
        