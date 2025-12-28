#Search insert position of K in a sorted array

class Solution:
    def searchInsertK(self, arr, k):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            # Calculate middle index
            mid = (low + high) // 2
            
            if arr[mid] == k:
                return mid
            
            elif arr[mid] < k:
                # Target is in the right half
                low = mid + 1
                
            else:
                # Target is in the left half
                high = mid - 1
        
        # If not found, 'low' is the correct insertion index
        return low
    
# Time Complexity: O(log n) due to binary search, where n is the number of elements in the array.
# Space Complexity: O(1) as we are using constant extra space.