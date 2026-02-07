class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        for i, pos in enumerate(position):
            hashmap[pos] = i

        count = block = 0
        for pos in sorted(hashmap, reverse=True):
            time = (target - pos) / speed[hashmap[pos]]
            if time > block:
                count += 1
                block = time

        return count
