#Count Inversions

class Solution:
    def inversionCount(self, arr):
        # A wrapper to call the recursive merge sort function
        temp_arr = [0] * len(arr)
        return self.merge_sort(arr, temp_arr, 0, len(arr) - 1)

    def merge_sort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            # Count inversions in left subarray
            inv_count += self.merge_sort(arr, temp_arr, left, mid)
            
            # Count inversions in right subarray
            inv_count += self.merge_sort(arr, temp_arr, mid + 1, right)
            
            # Count split inversions while merging
            inv_count += self.merge(arr, temp_arr, left, mid, right)
            
        return inv_count

    def merge(self, arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There is an inversion: arr[i] > arr[j]
                # Because the left subarray is sorted, if arr[i] > arr[j],
                # then all elements from i to mid are also > arr[j].
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
            
        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
            
        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
            
        # Copy the sorted subarray into Original array
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
            
        return inv_count
    
# Time Complexity: O(N log N) due to the divide and conquer approach of merge sort, where N is the number of elements in the array.
# Space Complexity: O(N) for the temporary array used during merging.