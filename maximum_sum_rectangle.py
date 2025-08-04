#Maximum sum Rectangle

class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')

        for left in range(m):
            temp = [0] * n

            for right in range(left, m):
                for i in range(n):
                    temp[i] += mat[i][right]

                # Apply Kadane's algorithm on temp
                curr_max = temp[0]
                curr_sum = temp[0]

                for k in range(1, n):
                    curr_sum = max(temp[k], curr_sum + temp[k])
                    curr_max = max(curr_max, curr_sum)

                max_sum = max(max_sum, curr_max)

        return max_sum

# Time Complexity: O(n * m^2)
# - O(m^2) for the two nested loops iterating over columns
# - O(n) for Kadane's algorithm applied on the temp array   

# Space Complexity: O(n)
# - O(n) for the temporary array used to store column sums     
# Where n = number of rows in the matrix. m = number of columns in the matrix