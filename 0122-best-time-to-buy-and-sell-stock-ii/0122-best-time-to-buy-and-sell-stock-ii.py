class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_total_profit = 0
        
        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, take the profit
            if prices[i] > prices[i-1]:
                max_total_profit += prices[i] - prices[i-1]
                
        return max_total_profit