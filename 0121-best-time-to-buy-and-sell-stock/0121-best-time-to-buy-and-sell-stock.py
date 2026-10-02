class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, max_profit = prices[0], 0

        for price in prices:
            profit = price - min_price
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                min_price = price

        return max_profit

        