class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scan
        # edge case: strs[i] is empty

        word = strs[0]
        n = len(word)
        for i in range(n):
            chr = word[i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != chr:
                    return word[:i]

        return word

        