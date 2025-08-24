#Check if frequencies can be equal

from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        freq_count = Counter(freq.values())
        
        if len(freq_count) == 1:
            # Case 1: All characters already have the same frequency
            return True
        
        if len(freq_count) == 2:
            key1, key2 = freq_count.keys()
            val1, val2 = freq_count[key1], freq_count[key2]
            
            # Case 2: One frequency occurs only once and it is 1 (e.g., {'a':3, 'b':3, 'c':1})
            if (key1 == 1 and val1 == 1) or (key2 == 1 and val2 == 1):
                return True
            
            # Case 3: One frequency is greater than the other by 1 and occurs only once
            if (abs(key1 - key2) == 1):
                if (key1 > key2 and freq_count[key1] == 1) or (key2 > key1 and freq_count[key2] == 1):
                    return True
        
        return False

#Time Complexity: O(n) where n is the length of the string
#Space Complexity: O(n) for the frequency counters