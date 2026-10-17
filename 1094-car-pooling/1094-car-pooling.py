class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for num, f, t in trips:
            diff[f] += num
            diff[t] -= num

        count = 0
        for num in diff:
            count += num
            if count > capacity:
                return False

        return True
        