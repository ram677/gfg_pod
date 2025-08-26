#Check if a String is Subsequence of Other

class Solution:
    def isSubSeq(self, s1: str, s2: str) -> bool:
        """
        Checks if s1 is a subsequence of s2 using a two-pointer approach.
        """
        # Get the lengths of the strings
        m = len(s1)
        n = len(s2)
        
        # Pointers for s1 and s2
        i = 0  # Pointer for the subsequence s1
        j = 0  # Pointer for the main string s2
        
        # Traverse both strings until one of them is exhausted
        while i < m and j < n:
            # If the characters match, move the pointer for s1
            if s1[i] == s2[j]:
                i += 1
            # Always move the pointer for s2 to scan through it
            j += 1
            
        # If the pointer 'i' has reached the end of s1,
        # it means all characters of s1 were found in order.
        return i == m

#Time Complexity: O(n), where n is the length of s2
#Space Complexity: O(1)