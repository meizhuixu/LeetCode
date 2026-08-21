class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        l = 0
        window = defaultdict(int)
        res = 0
        freq = 0


        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] > freq:
                freq = window[s[r]]

            if r - l + 1 - freq > k:
                window[s[l]] -= 1
                l += 1

        return r - l + 1