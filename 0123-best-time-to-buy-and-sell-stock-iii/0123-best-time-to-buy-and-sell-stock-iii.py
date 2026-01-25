class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        # Initial states
        # we use float('inf') for costs and 0 for profits
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0
        
        for price in prices:
            # 1. First Buy: Lowest price we've seen so far
            buy1 = min(buy1, price)
            
            # 2. First Sell: Max profit if we sold today
            sell1 = max(sell1, price - buy1)
            
            # 3. Second Buy: Lowest "effective" price 
            # (Current price minus profit already made from sell1)
            buy2 = min(buy2, price - sell1)
            
            # 4. Second Sell: Max total profit if we sold the second stock today
            sell2 = max(sell2, price - buy2)
            
        return sell2