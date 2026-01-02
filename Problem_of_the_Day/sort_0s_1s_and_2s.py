#Sort 0s, 1s and 2s

class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                # Swap 0 to the 'low' region
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 is already in the middle, just move forward
                mid += 1
            else:
                # Swap 2 to the 'high' region
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
                # Note: We do NOT increment mid here because the 
                # element swapped from 'high' hasn't been processed yet.

# Time Complexity: O(N), where N is the number of elements in the array.
# Space Complexity: O(1).