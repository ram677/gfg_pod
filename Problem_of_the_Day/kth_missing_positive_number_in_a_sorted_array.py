#Kth Missing Positive Number in a Sorted Array

class Solution:
    def kthMissing(self, arr, k):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Calculate how many positive integers are missing up to index 'mid'
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                # If fewer than k numbers are missing so far, the target is to the right
                low = mid + 1
            else:
                # If k or more numbers are missing, the target is to the left
                high = mid - 1
        
        # The k-th missing number is simply k + low
        return k + low