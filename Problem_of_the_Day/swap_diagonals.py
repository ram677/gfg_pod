#Swap diagonals

class Solution:
    def swapDiagonal(self, mat):
        n = len(mat)
        
        # Iterate through each row
        for i in range(n):
            # Swap the major diagonal element with the minor diagonal element
            # Major diagonal index: i
            # Minor diagonal index: n - 1 - i
            mat[i][i], mat[i][n - 1 - i] = mat[i][n - 1 - i], mat[i][i]
            
        # No explicit return needed as the operation is in-place,
        # but returning it is often helpful for verification.
        return mat
    
# Time Complexity: O(n), where n is the number of rows (or columns) in the matrix.
# Space Complexity: O(1), since we are modifying the matrix in place.