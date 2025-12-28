#Find the longest string

class Solution():
    def longestString(self, words):
        word_set = set(words)
        words.sort()  # Sort to handle lexicographical order
        longest = ""

        for word in words:
            is_valid = True
            # Check if all prefixes exist
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    is_valid = False
                    break
            if is_valid:
                # Update longest if this word is longer or lex smaller
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest

        
#Time Complexity: O(n * m) where n is the number of words and m is the average length of the words.
#Space Complexity: O(n) for the word set.
