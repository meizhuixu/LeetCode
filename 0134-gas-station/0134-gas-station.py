class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        count = total = start = 0

        for i in range(n):
            count += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if count < 0:
                count = 0
                start = i + 1

        return start if total >= 0 else -1