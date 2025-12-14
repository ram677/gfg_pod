#2D Submatrix Sum Queries

class Solution:
    def prefixSum2D(self, mat, queries):
        n = len(mat)
        m = len(mat[0])
        
        # Create a prefix sum matrix of size (n+1) x (m+1) filled with 0s
        # pref[i][j] will store the sum of the rectangle from (0,0) to (i-1, j-1) in mat
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Build the prefix sum matrix
        for i in range(n):
            for j in range(m):
                # pref[i+1][j+1] corresponds to the sum ending at mat[i][j]
                pref[i+1][j+1] = (mat[i][j] 
                                  + pref[i][j+1]   # Sum of the rectangle above
                                  + pref[i+1][j]   # Sum of the rectangle to the left
                                  - pref[i][j])    # Subtract the overlap (diagonal top-left)
        
        results = []
        for r1, c1, r2, c2 in queries:
            # Use the inclusion-exclusion principle to calculate the submatrix sum in O(1)
            # Note: Since pref is 1-based (padded), mat[r][c] corresponds to pref[r+1][c+1]
            
            total = pref[r2+1][c2+1]      # Sum from (0,0) to (r2, c2)
            top = pref[r1][c2+1]          # Area above the submatrix
            left = pref[r2+1][c1]         # Area to the left of the submatrix
            corner = pref[r1][c1]         # The intersection area subtracted twice
            
            submatrix_sum = total - top - left + corner
            results.append(submatrix_sum)
            
        return results
    
# Time Complexity: O(n * m + q), where n and m are the dimensions of the matrix, and q is the number of queries.
# Space Complexity: O(n * m), for the prefix sum matrix.