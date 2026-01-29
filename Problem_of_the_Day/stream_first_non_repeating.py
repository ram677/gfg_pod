#Stream First Non-repeating

from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = {}
        queue = deque()
        result = []
        
        for char in s:
            # 1. Update frequency
            freq[char] = freq.get(char, 0) + 1
            
            # 2. Add to queue only if it's the first time seeing this char
            # This optimization keeps the queue size smaller (max 26 unique chars)
            if freq[char] == 1:
                queue.append(char)
            
            # 3. Clean the front of the queue
            # Remove characters that have become repeating (freq > 1)
            while queue and freq[queue[0]] > 1:
                queue.popleft()
            
            # 4. Determine the answer for the current position
            if queue:
                result.append(queue[0])
            else:
                result.append('#')
                
        return "".join(result)
    
# Time Complexity: O(n) where n is the length of the string, as each character is processed once.
# Space Complexity: O(1) since the frequency dictionary and queue will hold at most 26 characters (assuming only lowercase letters).