#Count elements less than or equal to k in a sorted rotated array

import bisect

class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        
        # 1. Find the pivot (index of the minimum element) using Binary Search
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[hi]:
                # Minimum is in the right half
                lo = mid + 1
            else:
                # Minimum is at mid or in the left half
                hi = mid
        pivot = lo
        
        # 2. Count elements <= x in the first sorted segment (indices 0 to pivot-1)
        # bisect_right returns the insertion point, which equals the count of valid elements
        count1 = bisect.bisect_right(arr, x, lo=0, hi=pivot)
        
        # 3. Count elements <= x in the second sorted segment (indices pivot to n-1)
        # bisect_right returns the absolute index, so we subtract 'pivot' to get the local count
        idx2 = bisect.bisect_right(arr, x, lo=pivot, hi=n)
        count2 = idx2 - pivot
        
        return count1 + count2
    
# Time Complexity: O(log N) due to binary search for pivot and two bisect operations, where N is the size of the array.
# Space Complexity: O(1) additional space.