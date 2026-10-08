class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = []
        for _, h in envelopes:
            insert = bisect.bisect_left(tails, h)
            if insert == len(tails):
                tails.append(h)
            else:
                tails[insert] = h

        return len(tails)