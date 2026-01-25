class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize the minimum price to a very large number
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update min_price if we find a new low
            if price < min_price:
                min_price = price
            
            # Calculate profit if we sold at current price
            current_profit = price - min_price
            
            # Update max_profit if current_profit is higher
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit