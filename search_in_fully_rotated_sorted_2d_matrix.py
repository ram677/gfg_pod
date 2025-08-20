#Search in fully rotated sorted 2D matrix

class Solution:
    def searchMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        total = n * m
        left, right = 0, total - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, m)
            val = mat[row][col]

            if val == x:
                return True

            # find leftmost element
            lrow, lcol = divmod(left, m)
            rrow, rcol = divmod(right, m)
            left_val, right_val = mat[lrow][lcol], mat[rrow][rcol]

            if left_val <= val:  # left half sorted
                if left_val <= x < val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right half sorted
                if val < x <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False

#Time complexity: O(log(n * m))
#Space complexity: O(1)
#Where n is the number of rows and m is the number of columns in the matrix.