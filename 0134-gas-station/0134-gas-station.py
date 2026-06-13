class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, lowest = 0, float('inf')

        for i in range(n):
            total += gas[i] - cost[i]

            if total < lowest:
                lowest = total
                res = i + 1

        if total < 0:
            return -1

        return res if res < n else 0

        