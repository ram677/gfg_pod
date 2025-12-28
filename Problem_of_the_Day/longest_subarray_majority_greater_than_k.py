#Longest Subarray with Majority Greater than K

class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        max_len = 0
        first_occurrence = {}

        for i in range(n):
            # Convert based on comparison with k
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum > 0:
                max_len = i + 1
            else:
                if prefix_sum - 1 in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
    
#Time Complexity: O(n)
#Space Complexity: O(n) 
#Where n = len(arr) is the number of elements in the input array.