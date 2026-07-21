class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hashmap = defaultdict(int)

        for s, e in intervals:
            hashmap[s] += 1
            hashmap[e] -= 1

        res = cnt = 0
        for time in sorted(hashmap.keys()):
            cnt += hashmap[time]
            res = max(res, cnt)

        return res


        