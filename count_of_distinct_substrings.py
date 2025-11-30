#Count of distinct substrings

class Solution:
    def countSubs(self, s):
        # The root of our Trie
        root = {}
        count = 0
        n = len(s)
        
        # Iterate through every starting position of the string
        for i in range(n):
            node = root
            # Iterate through the rest of the string from position i
            for j in range(i, n):
                char = s[j]
                
                # If this path doesn't exist, it's a new distinct substring
                if char not in node:
                    node[char] = {}
                    count += 1
                
                # Move down the Trie
                node = node[char]
                
        return count
    
# Time Complexity: O(n^2) in the worst case, where n is the length of the string.
# Space Complexity: O(n^2) in the worst case, for storing the Trie.