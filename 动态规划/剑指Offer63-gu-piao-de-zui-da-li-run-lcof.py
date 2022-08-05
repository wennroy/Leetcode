class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        LeftMin = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < LeftMin:
                LeftMin = prices[i]
            elif max_profit < prices[i] - LeftMin:
                max_profit = prices[i] - LeftMin

        return max_profit

