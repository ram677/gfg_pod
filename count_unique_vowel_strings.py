#Count Unique Vowel Strings

import collections
import math

class Solution:
    def vowelCount(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        vowel_counts_in_s = collections.defaultdict(int)
        for char in s:
            if char in vowels:
                vowel_counts_in_s[char] += 1
        
        num_unique_vowels_present = 0
        product_of_vowel_occurrences = 1

        for vowel in vowels:
            if vowel_counts_in_s[vowel] > 0:
                num_unique_vowels_present += 1
                product_of_vowel_occurrences *= vowel_counts_in_s[vowel]
        
        if num_unique_vowels_present == 0:
            return 0
            
        permutations_of_unique_vowels = math.factorial(num_unique_vowels_present)
        
        total_distinct_strings = product_of_vowel_occurrences * permutations_of_unique_vowels
        
        return total_distinct_strings

#Time Complexity: O(n) where n is the length of the input string.
#Space Complexity: O(1) since we are using a constant amount of space.