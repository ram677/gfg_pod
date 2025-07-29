class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        
        rowSum = [sum(row) for row in mat]
        colSum = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        
        maxSum = max(max(rowSum), max(colSum))
        
        totalOps = 0
        
        # Traverse the matrix to balance rows and columns
        for i in range(n):
            for j in range(n):
                # Find how much we can increase this cell without exceeding target
                increment = min(maxSum - rowSum[i], maxSum - colSum[j])
                
                mat[i][j] += increment
                rowSum[i] += increment
                colSum[j] += increment
                totalOps += increment
        
        return totalOps
#Time Complexity: O(n²) where n is the matrix size