class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * n

        for f, l, s in bookings:
            diff[f-1] += s
            if l < n:
                diff[l] -= s

        count = 0
        for i in range(n):
            count += diff[i]
            diff[i] = count

        return diff
            
        