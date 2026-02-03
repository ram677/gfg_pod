#Stock Buy and Sell – Max one Transaction Allowed

class Solution:
    def maxProfit(self, prices):
        # Initialize min_price to infinity so the first price becomes the minimum
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # 1. Update the lowest price seen so far (Buying point)
            if price < min_price:
                min_price = price
            
            # 2. Calculate profit if we sold today and update max_profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
    
# Time Complexity: O(n), where n is the number of days (length of prices array).
# Space Complexity: O(1), as we are using only constant extra space.