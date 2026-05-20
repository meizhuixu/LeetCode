class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation:sliding window
        # s1 = "ab", s2 = "eidbaooo"
        #                     lr
        # seen = {b: 1, a: 1 }
        # match = 2
        # match == target: True
        # time: O(n)
        # space: O(1)

        window = defaultdict(int)
        need = Counter(s1)
        target = len(need)
        count = l = 0

        for r in range(len(s2)):
            char = s2[r]
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    count += 1

            if r - l + 1 > len(s1):
                drop = s2[l]
                if drop in need:
                    if window[drop] == need[drop]:
                        count -= 1
                    window[drop] -= 1

                l += 1

            if r - l + 1 == len(s1) and count == target:
                return True

        return False