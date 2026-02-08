#Find Kth Rotation

class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If the middle element is greater than the last element,
            # it means the smaller elements (the pivot) are in the right half.
            if arr[mid] > arr[high]:
                low = mid + 1
            # Otherwise, the minimum is either at 'mid' or in the left half.
            else:
                high = mid
                
        # 'low' will point to the minimum element's index, 
        # which is exactly the number of rotations.
        return low
    
# Time Complexity: O(log n) where n is the length of the input array, due to the binary search approach.
# Space Complexity: O(1) as we are using only constant extra space to store the indices.