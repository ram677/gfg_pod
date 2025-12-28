#Sum-string

class Solution:
    def isSumString(self, s):
        # Function to check if string can be split into sum-strings
        def backtrack(index, prev1, prev2):
            if index == len(s):  # Reached the end of the string
                return True

            # We try different lengths for the next number
            for length in range(1, len(s) - index + 1):
                # Get the current substring
                curr = s[index:index + length]

                # Check for leading zeros
                if len(curr) > 1 and curr[0] == '0':
                    continue

                # If the current substring is the sum of the previous two, continue
                if int(curr) == prev1 + prev2:
                    if backtrack(index + length, prev2, int(curr)):  # Try next part
                        return True
            return False

        # Try all possible initial splits (s1 and s2)
        for i in range(1, len(s)):
            for j in range(i + 1, len(s)):
                # Get first two substrings
                s1 = s[:i]
                s2 = s[i:j]

                # Check for leading zeros
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue

                # Call backtrack to check if the string can be formed
                if backtrack(j, int(s1), int(s2)):
                    return True

        return False

#Time Complexity: O(n^3) in the worst case, where n is the length of the string
#Space Complexity: O(n) for the recursion stack.