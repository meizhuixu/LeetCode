class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        for s, e in intervals:
            hashmap[s] += 1
            hashmap[e] -= 1

        count = result = 0
        for time in sorted(hashmap.keys()):
            count += hashmap[time]
            result = max(result, count)

        return result
