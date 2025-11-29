#Count set bits

class Solution:
    def countSetBits(self, n):
        # Base case
        if n == 0:
            return 0
        
        # Find the position of the Most Significant Bit (MSB)
        # For n=4 (100), x=2. For n=17 (10001), x=4.
        # This gives us the largest power of 2 less than or equal to n.
        x = n.bit_length() - 1
        
        # Calculate 2^x
        power_of_2 = 1 << x
        
        # 1. Count bits in the full group [0, 2^x - 1]
        # Formula: x * 2^(x-1)
        part1 = x * (power_of_2 >> 1)
        
        # 2. Count the MSBs for numbers in range [2^x, n]
        part2 = n - power_of_2 + 1
        
        # 3. Recursively count the remaining bits for [2^x, n]
        # (This corresponds to solving for the remainder: n - 2^x)
        part3 = self.countSetBits(n - power_of_2)
        
        return part1 + part2 + part3
    
# Time Complexity: O(log n), where n is the input number.
# Space Complexity: O(log n), for the recursive call stack.