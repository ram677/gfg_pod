#Game of XOR

class Solution:
    def subarrayXor(self, arr):
        n = len(arr)
        result = 0
        
        for i in range(n):
            # Calculate how many subarrays include the element at index i
            freq = (i + 1) * (n - i)
            
            # If the frequency is odd, it contributes to the total XOR
            if freq % 2 != 0:
                result ^= arr[i]
                
        return result

# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of extra space.