#Balancing Consonants and Vowels Ratio

from collections import defaultdict

class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        balance = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1  # Starting point

        for word in arr:
            v, c = 0, 0
            for ch in word:
                if ch in vowels:
                    v += 1
                else:
                    c += 1
            # Net change in balance
            balance += v - c
            count += freq[balance]
            freq[balance] += 1
        
        return count
    
#Time Complexity: O(m)
#Space Complexity: O(m)
#Where m = total number of characters in all strings in arr.
