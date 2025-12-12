#Transpose of Matrix

class Solution:
    def transpose(self, mat):
        n = len(mat)
        
        # Iterate through the rows
        for i in range(n):
            # Iterate through the columns starting from i + 1
            # to avoid swapping elements back and to skip the diagonal
            for j in range(i + 1, n):
                # Swap element at (i, j) with element at (j, i)
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                
        return mat
    
# Time Complexity: O(n^2), where n is the number of rows (or columns) in the matrix.
# Space Complexity: O(1), since we are modifying the matrix in place.