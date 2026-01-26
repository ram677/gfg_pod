#Generate Permutations of an array

class Solution:
    def permuteDist(self, arr):
        result = []
        n = len(arr)
        
        def backtrack(index):
            # Base case: if we have reached the end of the array,
            # we have found a valid permutation.
            if index == n:
                result.append(arr[:]) # Append a copy of the current array
                return
            
            # Iterate through the array starting from 'index'
            for i in range(index, n):
                # Swap the current element with the element at 'index'
                arr[index], arr[i] = arr[i], arr[index]
                
                # Recursively generate permutations for the rest of the array
                backtrack(index + 1)
                
                # Backtrack: undo the swap to restore the array for the next iteration
                arr[index], arr[i] = arr[i], arr[index]
        
        backtrack(0)
        return result
    
# Time Complexity: O(n * n!) where n is the length of the array.
# Space Complexity: O(n!) to store all the permutations.