#Missing Element in Range

class Solution:
    def missingRange(self, arr, low, high):
        # Convert array to a set for O(1) lookup time
        present_elements = set(arr)
        missing_elements = []
        
        # Iterate through the inclusive range [low, high]
        for num in range(low, high + 1):
            # If the number is not in our set, it's missing
            if num not in present_elements:
                missing_elements.append(num)
                
        return missing_elements
    
# Time Complexity: O(N + M) where N is the number of elements in the input array and M is the size of the range [low, high]. The set creation takes O(N) and the iteration through the range takes O(M).
# Space Complexity: O(N) for the set that stores the elements of the input array. The output list of missing elements can also take up to O(M) space in the worst case if all elements in the range are missing.