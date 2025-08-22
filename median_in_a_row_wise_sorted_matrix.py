#Median in a row-wise sorted Matrix

import bisect

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Define search range based on matrix min and max
        low = min(row[0] for row in mat)       # smallest element
        high = max(row[-1] for row in mat)     # largest element
        
        desired = (n * m + 1) // 2  # index of median in sorted order
        
        while low < high:
            mid = (low + high) // 2
            
            # Count how many elements <= mid
            count = 0
            for row in mat:
                # bisect_right gives index of first element > mid
                count += bisect.bisect_right(row, mid)
            
            # Adjust binary search range
            if count < desired:
                low = mid + 1
            else:
                high = mid
        
        return low

#Time Complexity: O(n log m log(max-min)).
#Space Complexity: O(1)
#Where n is the number of rows, m is the number of columns, and max and min are the maximum and minimum elements in the matrix, respectively.