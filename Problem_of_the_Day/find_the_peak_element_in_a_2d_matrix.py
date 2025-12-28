#Find the Peak Element in a 2D Matrix

class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = 0
        high = m - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Find the maximum element in the current 'mid' column
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            # Check left neighbor
            # If mid > 0 and left neighbor is greater, move to left half
            left_is_greater = False
            if mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]:
                left_is_greater = True
            
            # Check right neighbor
            # If mid < m-1 and right neighbor is greater, move to right half
            right_is_greater = False
            if mid < m - 1 and mat[max_row][mid + 1] > mat[max_row][mid]:
                right_is_greater = True
            
            if left_is_greater:
                high = mid - 1
            elif right_is_greater:
                low = mid + 1
            else:
                # If neither left nor right is greater, this is a peak
                return [max_row, mid]
                
        return [-1, -1]
    
# Time Complexity: O(n log m), where n is the number of rows and m is the number of columns in the matrix.
# Space Complexity: O(1).