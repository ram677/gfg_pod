#Tywin's War Strategy

import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        required = math.ceil(n / 2)  # troops that must be lucky
        
        # Step 1: Count already lucky troops
        lucky_count = sum(1 for x in arr if x % k == 0)
        if lucky_count >= required:
            return 0
        
        # Step 2: Calculate soldiers needed for each non-lucky troop
        needs = []
        for x in arr:
            if x % k != 0:
                needs.append(k - (x % k))
        
        # Step 3: Sort and pick cheapest ones
        needs.sort()
        soldiers_added = sum(needs[:required - lucky_count])
        
        return soldiers_added

#Time Complexity: O(n log n)
#Space Complexity: O(n)
#Where n is the number of troops.
#The space is mainly used for the 'needs' list which stores the additional soldiers needed for each non-lucky troop.