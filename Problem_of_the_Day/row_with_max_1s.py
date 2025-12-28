#Row with max 1s

import bisect

class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        if n == 0: return -1
        m = len(arr[0])
        
        max_row_index = -1
        # Start with the best possible column index as 'm' (out of bounds)
        min_col = m
        
        for i in range(n):
            # Optimization: 
            # Check if this row has a 1 at the position just left of our best found 1 so far.
            # If arr[i][min_col - 1] is 0, this row cannot strictly improve the result.
            # We also check min_col > 0 to handle the edge case where we've already found the best possible row.
            if min_col > 0 and arr[i][min_col - 1] == 1:
                
                # This row is a candidate. Find the FIRST occurrence of 1.
                # bisect_left uses binary search to find the insertion point of 1.
                # We limit the search range to 'min_col' because we only care about 1s to the left.
                idx = bisect.bisect_left(arr[i], 1, hi=min_col)
                
                # Update our best record
                min_col = idx
                max_row_index = i
                
                # Super Optimization: 
                # If we found a row starting with 1 at index 0 (all 1s), 
                # we can't possibly find a better row. Break immediately.
                if min_col == 0:
                    break
                    
        return max_row_index
    
# Time Complexity: O(N log M) in the worst case, where N is the number of rows and M is the number of columns.
# Space Complexity: O(1) additional space.