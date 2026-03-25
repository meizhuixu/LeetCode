class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        low, high = 0, max(inventory) + 1
        while low < high:
            mid = (low + high) // 2
            count_orders = sum(max(0, i - mid) for i in inventory)
            if count_orders <= orders:
                high = mid
            else:
                low = mid + 1

        lowest_price = high
        total_orders = profit = 0
        for i in inventory:
            if i > lowest_price:
                n = i - lowest_price
                total_orders += n
                profit += (lowest_price + 1 + i) * n // 2

        if total_orders < orders:
            profit += (orders - total_orders) * lowest_price

        return profit % (10 ** 9 + 7)
        

        


        