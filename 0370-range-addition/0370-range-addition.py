class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        diff = [0] * length
        for s, e, inc in updates:
            diff[s] += inc
            if e < length - 1:
                diff[e + 1] -= inc

        for i in range(1, length):
            diff[i] += diff[i - 1]

        return diff

        