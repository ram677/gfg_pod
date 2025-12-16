#Strings Rotations of Each Other

class Solution:
    def areRotations(self, s1, s2):
        # If lengths are different, they cannot be rotations
        if len(s1) != len(s2):
            return False
            
        # Check if s2 is a substring of s1 concatenated with itself
        # This covers all possible circular shifts
        return s2 in (s1 + s1)

# Time Complexity: O(n) where n is the length of the strings.
# Space Complexity: O(n) for the concatenated string.