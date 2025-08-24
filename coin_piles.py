#Coin Piles

import bisect

class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)
        
        # Prefix sum for total coins
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        res = float('inf')
        
        for i in range(n):
            x = arr[i]
            y = x + k
            
            # Index of first pile > y
            upper = bisect.bisect_right(arr, y)
            
            # Coins to remove:
            # 1. All coins before i (less than x)
            coins_removed_left = prefix[i]
            # 2. Excess coins from piles > y
            coins_removed_right = prefix[n] - prefix[upper] - (n - upper) * y
            
            total_removed = coins_removed_left + coins_removed_right
            res = min(res, total_removed)
        
        return res

    #Time Complexity: O(n log n) where n is the number of piles
    #Space Complexity: O(n) for the prefix sum array