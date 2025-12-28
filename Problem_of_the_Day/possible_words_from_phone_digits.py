#Possible Words From Phone Digits

from typing import List

class Solution:
  def possibleWords(self, arr: List[int]) -> List[str]:
    keypad_map = {
      2: "abc",
      3: "def",
      4: "ghi",
      5: "jkl",
      6: "mno",
      7: "pqrs",
      8: "tuv",
      9: "wxyz"
    }
    
    result = []
    n = len(arr)
    
    def backtrack(index: int, current_word: str):
      # Base case: If we have processed all digits, we have a complete word.
      if index == n:
        # Only add non-empty words to the result.
        if current_word:
          result.append(current_word)
        return
      
      current_digit = arr[index]
      
      # If the digit has a letter mapping, iterate through its letters.
      if current_digit in keypad_map:
        letters = keypad_map[current_digit]
        for letter in letters:
          # Recurse by appending the letter and moving to the next digit.
          backtrack(index + 1, current_word + letter)
      # If the digit has no mapping (like 0 or 1), just skip it.
      else:
        # Recurse by moving to the next digit without changing the word.
        backtrack(index + 1, current_word)

    # Start the backtracking process.
    if n > 0:
        backtrack(0, "")
    
    return result
  
# Time Complexity: O(4^n) in the worst case, where n is the number of digits. This occurs when all digits are 7 or 9, which map to 4 letters each.
# Space Complexity: O(n) for the recursion stack and the space used to store the combinations in the result.