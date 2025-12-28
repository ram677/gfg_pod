class Solution:
    def asciirange(self, s):
        first = {}
        last = {}
        
        # Record first and last occurrences of each character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        result = []

        # Iterate over characters that appear more than once
        for ch in first:
            if first[ch] != last[ch]:
                start = first[ch] + 1
                end = last[ch]
                total = sum(ord(s[i]) for i in range(start, end))
                if total > 0:
                    result.append(total)

        return result

#Time Complexity: O(n)
#Space Complexity: O(1)
#n = len(s)