class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        for s, e in intervals:
            hashmap[s] += 1
            hashmap[e] -= 1

        count = res = 0
        for t in sorted(hashmap.keys()):
            count += hashmap[t]
            res = max(res, count)
        return res