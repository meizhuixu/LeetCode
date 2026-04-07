class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = cur = total = 0

        for i in range(len(gas)):
            cur = max(cur, cur + gas[i] - cost[i])
            total += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i + 1

        return start if total >= 0 else -1

        