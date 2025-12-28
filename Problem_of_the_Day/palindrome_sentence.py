#Palindrome Sentence

class Solution:
    def isPalinSent(self, s):
        # Step 1: Filter and normalize the string
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        
        # Step 2: Check if it's a palindrome
        return cleaned == cleaned[::-1]

# Time Complexity: O(n) for both filtering and comparing.
# Space Complexity: O(n) for the cleaned string.
# Where n is the length of the input string s.