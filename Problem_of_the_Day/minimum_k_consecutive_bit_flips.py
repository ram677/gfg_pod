#Minimum K Consecutive Bit Flips

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        
        # 'current_flips' tracks the number of ongoing flip operations that affect the current index.
        current_flips = 0
        
        # 'total_flips' is the result we want to return.
        total_flips = 0
        
        for i in range(n):
            # When the sliding window moves, the effect of a flip started at arr[i-k] expires.
            # We use a value of 2 as a marker to indicate a flip started at that index.
            if i >= k and arr[i-k] == 2:
                current_flips -= 1
            
            # Determine if the current bit needs to be flipped.
            # The effective value of arr[i] is 0 if its original value has the same parity
            # as the number of flips affecting it.
            if (current_flips % 2) == arr[i]:
                # If a flip is needed but the window would exceed the array bounds, it's impossible.
                if i + k > n:
                    return -1
                
                # Otherwise, perform the flip.
                current_flips += 1
                total_flips += 1
                # Mark the start of this flip in-place.
                arr[i] = 2
        
        return total_flips

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(1) as we are using the input array for marking flips.