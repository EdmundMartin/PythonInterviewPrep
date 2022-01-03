from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        min_price = float("inf")

        for stock_price in prices:
            if stock_price < min_price:
                min_price = stock_price
            if stock_price > min_price:
                profit = stock_price - min_price
                if profit > max_profit:
                    max_profit = profit
        if max_profit == float("-inf"):
            return 0
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    assert result == 5

    prices = [7, 6, 4, 3, 1]
    result = Solution().maxProfit(prices)
    assert result == 0
