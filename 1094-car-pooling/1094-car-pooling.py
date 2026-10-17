class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        diff = [0] * 1002

        for num, f, t in trips:
            diff[f] += num
            diff[t] -= num

        count = 0
        for i in range(1002):
            count += diff[i]
            if count > capacity:
                return False

        return True
        