#Max sum in the configuration

class Solution:
    def maxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # Calculate the sum of all elements
        total_sum = sum(arr)
        
        # Calculate the initial value of i * arr[i]
        curr_val = sum(i * arr[i] for i in range(n))
        
        max_val = curr_val
        
        # Iterate to calculate the value for subsequent rotations
        # We simulate rotating the array to the left one by one
        for i in range(n - 1):
            # Formula: Next Val = Current Val + Total Sum - N * (Element being moved to end)
            # When we rotate left, arr[i] moves from index 0 to index n-1.
            # Its contribution changes from 0 to (n-1)*arr[i], but strictly speaking
            # the formula derived S_{next} = S_{curr} - (sum - arr[i]) + (n-1)*arr[i]
            # simplifies to S_{next} = S_{curr} - sum + n*arr[i] if rotating right.
            # Let's stick to the prompt's likely rotation definition.
            
            # Using the formula derived for left rotation:
            # The element at arr[i] is currently at the "front" (relative 0 index)
            # It moves to the back (index n-1). All other elements shift left (index - 1).
            # So they lose 1 * value. The one moving to back gains (n-1) * value.
            # Change = - (total_sum - arr[i]) + (n-1) * arr[i]
            # Change = - total_sum + arr[i] + n*arr[i] - arr[i]
            # Change = n*arr[i] - total_sum
            
            next_val = curr_val + (n * arr[i]) - total_sum
            
            if next_val > max_val:
                max_val = next_val
                
            curr_val = next_val
            
        return max_val
    
# Time Complexity: O(n) for calculating the initial sum and iterating through the array.
# Space Complexity: O(1) as we are using only constant extra space.