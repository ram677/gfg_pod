#Postfix Evaluation

class Solution:
    def evaluatePostfix(self, arr):
        # This list will function as our stack.
        stack = []
        
        # A set for quick lookups to see if a token is an operator.
        operators = {"+", "-", "*", "/", "^"}

        # Iterate through each token in the input array.
        for token in arr:
            if token in operators:
                # If the token is an operator, pop the top two operands.
                # The first one popped is the right-hand operand (op2).
                op2 = stack.pop()
                # The second one popped is the left-hand operand (op1).
                op1 = stack.pop()
                
                # Perform the operation based on the operator token.
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    # Use integer division // which performs floor division
                    # as required by the problem description.
                    stack.append(op1 // op2)
                elif token == '^':
                    # Use ** for exponentiation.
                    stack.append(op1 ** op2)
            else:
                # If the token is a number, convert it to an integer and
                # push it onto the stack.
                stack.append(int(token))
        
        # The final result is the single element remaining in the stack.
        return stack[0]
    
#Time Complexity: O(n) where n is the number of tokens in the input array. Each token is processed exactly once.
#Space Complexity: O(n) in the worst case, where all tokens are numbers and are pushed onto the stack.