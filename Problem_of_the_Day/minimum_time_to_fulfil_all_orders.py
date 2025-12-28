#Minimum time to fulfil all orders

import math

class Solution:
    def minTime(self, ranks, n):
        # Helper function to check if it's possible to make 'n' donuts in 'time_limit'
        def can_make_donuts(time_limit):
            total_donuts = 0
            for r in ranks:
                # Calculate how many donuts a chef with rank 'r' can make in 'time_limit'
                # Time taken for x donuts = r * (x * (x + 1)) / 2
                # We need to find max x such that r * x * (x + 1) / 2 <= time_limit
                # This leads to the quadratic inequality: x^2 + x - (2 * time_limit / r) <= 0
                # Solving x using quadratic formula: x = (-1 + sqrt(1 + 8 * time_limit / r)) / 2
                
                # Calculate the discriminant part inside sqrt
                val = 1 + (8 * time_limit) / r
                
                # Calculate x (number of donuts)
                donuts = int((-1 + math.isqrt(val)) // 2)
                
                total_donuts += donuts
                if total_donuts >= n:
                    return True
            return False

        # Binary Search for the minimum time
        # Lower bound: 0
        # Upper bound: Time for the fastest chef (min rank) to make all n donuts alone
        # Worst case rank is 100, max n is 1000. 
        # Time = 100 * 1000 * 1001 / 2 approx 5 * 10^7. So 10^8 is safe.
        low = 0
        high = min(ranks) * n * (n + 1) // 2
        
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_make_donuts(mid):
                ans = mid
                high = mid - 1  # Try for a smaller time
            else:
                low = mid + 1   # Need more time
                
        return ans

# Time Complexity: O(m log T) where m is the number of chefs (length of ranks) and T is the search space for time.
# Space Complexity: O(1).