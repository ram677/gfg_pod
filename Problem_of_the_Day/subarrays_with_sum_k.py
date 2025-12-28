class Solution:
    def cntSubarrays(self, arr, k):
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in arr:
            prefix_sum += num
            
            # Check if there is a prefix sum that satisfies the condition
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]
                
            # Update the prefix_sum count
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count
# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(n) 