#Expression Add Operators

from typing import List

class Solution:
  def findExpr(self, s: str, target: int) -> List[str]:
    n = len(s)
    result = []

    def backtrack(index: int, path: str, current_value: int, last_operand: int):
      # Base case: we've processed the entire string
      if index == n:
        if current_value == target:
          result.append(path)
        return

      # Recursive step: form the next operand and try all operators
      for j in range(index, n):
        current_operand_str = s[index : j + 1]
        
        # Pruning for numbers with leading zeros (e.g., "05")
        if len(current_operand_str) > 1 and current_operand_str[0] == '0':
          break
        
        current_operand_val = int(current_operand_str)

        # If this is the first number in the expression
        if index == 0:
          backtrack(j + 1,
                    current_operand_str,
                    current_operand_val,
                    current_operand_val)
        else:
          # Try '+' operator
          backtrack(j + 1,
                    path + "+" + current_operand_str,
                    current_value + current_operand_val,
                    current_operand_val)

          # Try '-' operator
          backtrack(j + 1,
                    path + "-" + current_operand_str,
                    current_value - current_operand_val,
                    -current_operand_val)

          # Try '*' operator
          backtrack(j + 1,
                    path + "*" + current_operand_str,
                    (current_value - last_operand) + (last_operand * current_operand_val),
                    last_operand * current_operand_val)

    backtrack(0, "", 0, 0)
    return result
  
# Time Complexity: O(4^n) in the worst case, where n is the length of the string. This is because at each position we can choose to add one of three operators or no operator (to form multi-digit numbers).
# Space Complexity: O(n) for the recursion stack and the space used to store the expressions in the result.