#Smallest window containing all characters

import collections

class Solution:
    def smallestWindow(self, s: str, p: str) -> str:
        # Edge case: If the pattern is longer than the string, it's impossible.
        if len(p) > len(s):
            return ""

        # Create a frequency map of the pattern string 'p'.
        p_map = collections.Counter(p)
        required_chars = len(p_map)
        
        # Sliding window variables
        left = 0
        formed_chars = 0
        window_counts = collections.defaultdict(int)
        
        # Variables to store the result
        min_len = float('inf')
        result_start_index = -1

        for right, char in enumerate(s):
            # Add the new character from the right to the window
            window_counts[char] += 1
            
            # If the character is needed and we've met its required count,
            # increment the count of satisfied characters.
            if char in p_map and window_counts[char] == p_map[char]:
                formed_chars += 1
            
            # Once the window is valid, try to shrink it from the left
            while left <= right and formed_chars == required_chars:
                current_len = right - left + 1
                
                # If we've found a new minimum length, update our result
                if current_len < min_len:
                    min_len = current_len
                    result_start_index = left
                
                # Remove the leftmost character to shrink the window
                char_left = s[left]
                window_counts[char_left] -= 1
                
                # If removing the character made the window invalid,
                # decrement the count of satisfied characters.
                if char_left in p_map and window_counts[char_left] < p_map[char_left]:
                    formed_chars -= 1
                    
                # Move the left pointer
                left += 1
        
        # If no valid window was ever found, return an empty string
        if result_start_index == -1:
            return ""
        else:
            return s[result_start_index : result_start_index + min_len]
        
#Time Complexity: O(n + m)
#Space Complexity: O(m)
#Where n is the length of the input string s and m is the length of the pattern string p.