#Decode the string

class Solution:
    def decodedString(self, s: str) -> str:
        # The stack will store tuples of (string_so_far, repetition_count)
        # for each level of nesting.
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                # Build the multi-digit number for the repetition count.
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # This marks the beginning of a new substring pattern.
                # We save the state of the current level (the string built so far
                # and the repeat count for the new pattern) onto the stack.
                stack.append((current_str, current_num))
                
                # Reset the state to build the new, nested substring.
                current_str = ""
                current_num = 0
            elif char == ']':
                # This marks the end of a substring pattern.
                # We pop the state of the parent string and its repeat count.
                prev_str, k = stack.pop()
                
                # The current_str at this point is the substring inside the brackets.
                # We repeat it 'k' times and prepend the parent string to it.
                current_str = prev_str + current_str * k
            else: # The character is a letter
                # Append the letter to the substring being built at the current level.
                current_str += char

        return current_str
    
#Time Complexity: O(n * k) where n is the length of the input string and k is the maximum number of repetitions for any substring. In the worst case, we may need to repeat a substring multiple times, leading to this complexity.
#Space Complexity: O(m) where m is the maximum depth of nested brackets in the input string. This space is used by the stack to store the state of each level of nesting.
# Additionally, the output string can also take up to O(n * k) space in the worst case, but this is not counted in space complexity as it is the output.    