#Count pairs Sum in matrices

class Solution:
    def countPairs(self, mat1, mat2, x):
        n = len(mat1)
        arr1 = [mat1[i][j] for i in range(n) for j in range(n)]
        arr2 = [mat2[i][j] for i in range(n) for j in range(n)]
        
        i, j = 0, len(arr2) - 1
        count = 0
        
        while i < len(arr1) and j >= 0:
            sum_ = arr1[i] + arr2[j]
            if sum_ == x:
                count += 1
                i += 1
                j -= 1
            elif sum_ < x:
                i += 1
            else:
                j -= 1
        
        return count

#Time Complexity: O(n^2) where n is the matrix size
#Space Complexity: O(n) for the flattened arrays
