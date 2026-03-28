class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        freqs = list(Counter(balls).values())

        x = min(freqs)
        while x >= 1:
            valid = True
            for f in freqs:
                group = f // x
                mod = f % x
                if mod > group:
                    x -= 1
                    valid = False
                    break

            res = 0
            if valid:
                for f in freqs:
                    res += (f + x) // (x + 1)
                return res

        