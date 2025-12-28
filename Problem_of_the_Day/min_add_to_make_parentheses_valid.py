#Min Add to Make Parentheses Valid

class Solution:
    def minParentheses(self, s: str) -> int:
        # Counts required '(' for invalid ')' found so far.
        additions = 0
        # Counts unmatched open parentheses '(' waiting for a ')'.
        balance = 0
        
        for char in s:
            if char == '(':
                # We have an open parenthesis, it needs a closing one.
                balance += 1
            else: # char == ')'
                # We have a closing parenthesis, it needs an open one.
                if balance > 0:
                    # We have a waiting open parenthesis, so use it.
                    balance -= 1
                else:
                    # No waiting open parenthesis, so this ')' is invalid.
                    # We must add a '(' to match it.
                    additions += 1
        
        # After the loop, `balance` is the number of open parentheses
        # that were never closed. We need to add a ')' for each.
        # The total is the sum of required '(' and required ')'.
        return additions + balance
    
#Time Complexity: O(n) where n is the length of the string.
#Space Complexity: O(1) since we are using only a fixed amount of extra space.