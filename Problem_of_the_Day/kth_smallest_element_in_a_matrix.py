#Kth smallest element in a Matrix

class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        low = mat[0][0]
        high = mat[n-1][n-1]
        
        while low < high:
            mid = (low + high) // 2
            
            # Count elements <= mid
            count = 0
            row = 0
            col = n - 1
            
            while row < n and col >= 0:
                if mat[row][col] <= mid:
                    # All elements to the left (including this one) are <= mid
                    count += (col + 1)
                    row += 1
                else:
                    # Current element is too big, move left
                    col -= 1
            
            if count < k:
                low = mid + 1
            else:
                high = mid
                
        return low
    
# Time Complexity: O(n log(max - min))) where n is the number of rows (or columns) in the matrix, and max and min are the maximum and minimum elements in the matrix.
# Space Complexity: O(1).