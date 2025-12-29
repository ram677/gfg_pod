#K-th element of two Arrays

class Solution:
    def kthElement(self, a, b, k):
        n = len(a)
        m = len(b)
        
        # Ensure 'a' is the smaller array to minimize binary search range
        if n > m:
            return self.kthElement(b, a, k)
            
        # Range for binary search on 'a'
        # low: max(0, k - m) -> If b is too small to cover all k, we MUST take some from a
        # high: min(k, n) -> We can't take more than k or more than available in a
        low = max(0, k - m)
        high = min(k, n)
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1
            
            # Handle edge cases where cuts are at the boundaries (0 or length)
            # l1, l2 are the elements just BEFORE the cut
            # r1, r2 are the elements just AFTER the cut
            l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]
            r1 = float('inf') if cut1 == n else a[cut1]
            r2 = float('inf') if cut2 == m else b[cut2]
            
            # Check if this partition is valid
            if l1 <= r2 and l2 <= r1:
                # We found the valid partition. The k-th element is the max of the left side.
                return max(l1, l2)
            elif l1 > r2:
                # Too many elements from 'a', move left
                high = cut1 - 1
            else:
                # Too few elements from 'a', move right
                low = cut1 + 1
                
        return 1
    
# Time Complexity: O(log(min(n, m))), where n and m are the sizes of the two arrays.
# Space Complexity: O(1).