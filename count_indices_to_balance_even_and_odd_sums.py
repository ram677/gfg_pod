#Count Indices to Balance Even and Odd Sums

class Solution:
    def cntWays(self, arr):
        n = len(arr)
        total_even = 0
        total_odd = 0
        
        # Step 1: Calculate total sums for even and odd indices
        for i in range(n):
            if i % 2 == 0:
                total_even += arr[i]
            else:
                total_odd += arr[i]
                
        curr_even = 0
        curr_odd = 0
        count = 0
        
        # Step 2: Iterate through the array to check each index
        for i in range(n):
            # Calculate remaining sums (suffix sums) after index i
            if i % 2 == 0:
                # If current index is even, remove it from the even total
                rem_even = total_even - curr_even - arr[i]
                rem_odd = total_odd - curr_odd
            else:
                # If current index is odd, remove it from the odd total
                rem_even = total_even - curr_even
                rem_odd = total_odd - curr_odd - arr[i]
            
            # Step 3: Form new sums based on the shift
            # Suffix odd elements become even-indexed, Suffix even elements become odd-indexed
            new_even_sum = curr_even + rem_odd
            new_odd_sum = curr_odd + rem_even
            
            if new_even_sum == new_odd_sum:
                count += 1
                
            # Step 4: Update prefix sums for the next iteration
            if i % 2 == 0:
                curr_even += arr[i]
            else:
                curr_odd += arr[i]
                
        return count
    
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), as we are using a constant amount of extra space.