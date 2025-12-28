#Array Duplicates

class Solution:
    def findDuplicates(self, arr):
        res = []
        
        for num in arr:
            # Map the value to an index (1 -> 0, 2 -> 1, etc.)
            index = abs(num) - 1
            
            # If the value at this index is negative, we have seen 'index + 1' before
            if arr[index] < 0:
                res.append(abs(num))
            else:
                # Mark this index as visited by negating the value
                arr[index] = -arr[index]
                
        return res
    
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), since we are modifying the input array in place.