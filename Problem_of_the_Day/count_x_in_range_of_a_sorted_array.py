#Count X in Range of a Sorted Array

from bisect import bisect_left, bisect_right

class Solution:
    def countXInRange(self, arr, queries):
        results = []
        for l, r, x in queries:
            # 1. Find the global start and end indices of x in the sorted array
            # i is the first index where arr[i] >= x
            i = bisect_left(arr, x)
            # j is the last index where arr[j] == x (bisect_right returns insertion point after x)
            j = bisect_right(arr, x) - 1
            
            # Check if x is present in the array at all
            if i <= j:
                # 2. Find the intersection of the range of x [i, j] and the query range [l, r]
                start = max(l, i)
                end = min(r, j)
                
                # 3. If the intersection is valid, calculate the count
                if start <= end:
                    results.append(end - start + 1)
                else:
                    results.append(0)
            else:
                # x is not in arr
                results.append(0)
                
        return results
    
# Time Complexity: O(Q log N) where Q is the number of queries and N is the size of the array.
# Space Complexity: O(1) additional space (excluding the output list).