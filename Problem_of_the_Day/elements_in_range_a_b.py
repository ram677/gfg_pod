#Elements in range [a, b]

from bisect import bisect_left, bisect_right

class Solution:
    def cntInRange(self, arr, queries):
        # Sort the array to enable binary search
        arr.sort()
        results = []
        
        for a, b in queries:
            # Find the first index where value >= a
            l = bisect_left(arr, a)
            
            # Find the first index where value > b
            # (This gives us the upper bound index, non-inclusive)
            r = bisect_right(arr, b)
            
            # The number of elements in range [a, b] is simply the difference
            results.append(r - l)
            
        return results
    
# Time Complexity: O(Q log N) for Q queries on an array of size N (due to sorting and binary searches).
# Space Complexity: O(1) additional space, ignoring the output list.