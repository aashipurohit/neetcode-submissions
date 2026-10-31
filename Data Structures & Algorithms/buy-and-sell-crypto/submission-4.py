class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0
        for price_today in prices:
            if price > price_today:
                price = price_today
            else:
                z = price_today - price
                if profit < z:
                    profit = z
        return profit

