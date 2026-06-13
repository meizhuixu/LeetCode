class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, lowest = 0, float('inf')

        for i in range(n):
            total = total + gas[i] - cost[i]

            if total < lowest:
                lowest = total
                res = i

        return res + 1 if total >= 0 else -1

        