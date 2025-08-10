#Palindrome SubStrings

class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        
        # Helper to expand around a center and count palindromes
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:  # length >= 2
                    count += 1
                l -= 1
                r += 1
        
        # Odd-length and even-length palindromes
        for center in range(n):
            # Odd length: center at index
            expand(center, center)
            # Even length: center between indices
            expand(center, center + 1)
        
        return count

# Time Complexity: O(n^2) where n is the length of the string
# Space Complexity: O(1) since we are using a constant amount of extra space    
# Where n is the length of the input string.