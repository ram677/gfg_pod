#Set Matrix Zeros

class Solution:
    def setMatrixZeroes(self, mat):
        if not mat or not mat[0]:
            return

        n = len(mat)
        m = len(mat[0])
        zero_rows = set()
        zero_cols = set()

        # First pass: identify rows and columns to be zeroed
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: update matrix
        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_cols:
                    mat[i][j] = 0

#Time Complexity: O(n * m) where n is the number of rows and m is the number of columns.
#Space Complexity: O(1) since we are using a constant amount of space.