#Happiest Triplet

class Solution:
    def smallestDiff(self, a, b, c):
        # Sort all three arrays to apply the three-pointer technique
        a.sort()
        b.sort()
        c.sort()
        
        # Initialize pointers
        i, j, k = 0, 0, 0
        n_a, n_b, n_c = len(a), len(b), len(c)
        
        # Initialize tracking variables for the best solution
        min_diff = float('inf')
        min_sum = float('inf')
        res = []
        
        # Iterate until one of the arrays is exhausted
        while i < n_a and j < n_b and k < n_c:
            val_a = a[i]
            val_b = b[j]
            val_c = c[k]
            
            # Calculate current stats
            curr_min = min(val_a, val_b, val_c)
            curr_max = max(val_a, val_b, val_c)
            curr_diff = curr_max - curr_min
            curr_sum = val_a + val_b + val_c
            
            # Update best result based on difference, then sum
            if curr_diff < min_diff:
                min_diff = curr_diff
                min_sum = curr_sum
                res = [val_a, val_b, val_c]
            elif curr_diff == min_diff:
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    res = [val_a, val_b, val_c]
            
            # Advance the pointer of the minimum value to try and shrink the range
            if val_a == curr_min:
                i += 1
            elif val_b == curr_min:
                j += 1
            else:
                k += 1
                
        # Return the resulting triplet in decreasing order
        res.sort(reverse=True)
        return res
    
# Time Complexity: O(n log n + m log m + p log p) due to sorting, where n, m, p are the lengths of the three arrays.
# Space Complexity: O(1) for the pointers and tracking variables, O(3) for the result triplet.