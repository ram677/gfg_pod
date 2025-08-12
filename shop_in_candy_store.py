#Shop in Candy Store

class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)
        
        # Minimum cost
        min_cost = 0
        i, j = 0, n - 1
        while i <= j:
            min_cost += prices[i]
            i += 1
            j -= k  # take k freebies from the end
        
        # Maximum cost
        max_cost = 0
        i, j = 0, n - 1
        while i <= j:
            max_cost += prices[j]
            j -= 1
            i += k  # take k freebies from the start
        
        return [min_cost, max_cost]

#Time Complexity: O(n log n)
#Space Complexity: O(1) 
#Where n is the number of candy prices.