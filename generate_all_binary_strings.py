#Generate all binary strings

from typing import List

class Solution:
  def binstr(self, n: int) -> List[str]:
    # This list will store the final binary strings.
    result = []
    
    # We define a helper function to perform the recursion.
    def generate(current_string: str):
      # Base Case: If the string's length equals n, we've found a valid string.
      if len(current_string) == n:
        result.append(current_string)
        return
      
      # Recursive Step 1: Explore the path by adding a '0'.
      generate(current_string + "0")
      
      # Recursive Step 2: Explore the path by adding a '1'.
      generate(current_string + "1")

    # Start the recursive generation with an empty string.
    generate("")
    
    return result
  
#Time Complexity: O(2^n) where n is the length of the binary strings to be generated.
#Space Complexity: O(n) for the recursion stack and the space used to store the binary strings.
# The output list will contain 2^n binary strings, each of length n.