class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # {a: 1, b: 1}
        count_s1 = Counter(s1)
        count_win = defaultdict(int)
        l = res = 0

        for r in range(len(s2)):
            cur = s2[r]
            count_win[cur] += 1
            if count_win[cur] == count_s1[cur]:
                res += 1

            if r - l + 1 > len(s1):
                drop = s2[l]
                if count_win[drop] == count_s1[drop]:
                    res -= 1
                count_win[drop] -= 1
                l += 1

            if res == len(count_s1):
                return True

        return False

        
        