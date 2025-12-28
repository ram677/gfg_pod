#Koko Eating Bananas

import math

class Solution:
    def kokoEat(self, arr, k):
        left, right = 1, max(arr)
        
        def canFinish(speed):
            total_hours = 0
            for pile in arr:
                total_hours += math.ceil(pile / speed)
                if total_hours > k:
                    return False
            return total_hours <= k
        
        while left < right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

#Time Complexity: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile
#Space Complexity: O(1) for the variables used