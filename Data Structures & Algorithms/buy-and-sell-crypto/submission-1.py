class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = 0

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[min_left] > max_profit:
                max_profit = prices[i] - prices[min_left]

            if prices[i] < prices[min_left]:
                min_left = i
        
        if max_profit > 0:
            return max_profit
        else:
            return 0

