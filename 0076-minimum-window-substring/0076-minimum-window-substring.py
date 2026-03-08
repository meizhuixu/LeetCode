class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # pruning
        if len(s) < len(t):
            return ''

        res = (-1, float('inf'))
        l = match = 0
        need = Counter(t) # store the counts of characters in t
        window = defaultdict(int) # track characters in the current window
        
        # iterate through string s by moving the right pointer
        for r in range(len(s)):
            if s[r] in need: # If the current character is part of t
                window[s[r]] += 1 # add it to my window count
                # When a character's frequency in the window matches its frequency in t, I'll increment a match counter
                if window[s[r]] == need[s[r]]:
                    match += 1

            # Once the match count equals the number of unique characters in t, it means the current window is valid
            # minimize the window by moving the left pointer forward as long as the window remains valid
            while match == len(need):
                # Whenever I find a valid window, I'll compare its length with the minimum length found so far and update my result.
                if r - l + 1 < res[1]:
                    res = (l, r - l + 1)
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1

        return '' if res[0] == -1 else s[res[0]: res[0] + res[1]]