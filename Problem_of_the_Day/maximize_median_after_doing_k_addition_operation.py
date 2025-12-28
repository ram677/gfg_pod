#Maximize median after doing k addition operation

class Solution:
    def maximizeMedian(self, arr, k):
        n = len(arr)
        arr.sort()

        median_idx = (n - 1) // 2
        new_val_of_first_median_elem = arr[median_idx]
        count = 1

        for i in range(median_idx + 1, n):
            diff = arr[i] - new_val_of_first_median_elem
            cost = count * diff

            if cost <= k:
                k -= cost
                new_val_of_first_median_elem = arr[i]
                count += 1
            else:
                increase = k // count
                new_val_of_first_median_elem += increase
                k = 0
                break

        if k > 0:
            increase = k // count
            new_val_of_first_median_elem += increase

        if n % 2 == 1:
            return new_val_of_first_median_elem
        else:
            if count > 1:
                return new_val_of_first_median_elem
            else:
                second_middle_val = arr[median_idx + 1]
                return (new_val_of_first_median_elem + second_middle_val) // 2

#Time Complexity: O(n log n) for sorting the array
#Space Complexity: O(1) for using constant extra space
# where n is the length of the array
# The algorithm only uses a fixed amount of extra space for variables, regardless of the input size.