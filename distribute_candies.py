#Distribute Candies

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        # We use an instance variable to accumulate the total moves.
        self.moves = 0

        def dfs(node):
            """
            Performs a post-order traversal.
            Returns the candy balance of the subtree rooted at 'node'.
            A positive balance means an excess of candies to be passed up.
            A negative balance means a deficit of candies to be received.
            """
            # Base case: An empty subtree has a balance of 0.
            if not node:
                return 0

            # 1. Recursively find the balance of the left and right subtrees.
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            # 2. The number of moves is the total flow of candies across the edges
            # to the left and right children. This is the sum of the absolute
            # values of their balances.
            self.moves += abs(left_balance) + abs(right_balance)

            # 3. Return the balance of the current subtree to its parent.
            # This is its own candies, plus the net from its children, minus the one it keeps.
            return node.data + left_balance + right_balance - 1

        # Start the traversal from the root.
        dfs(root)
        return self.moves
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(H) where H is the height of the binary tree (due to recursion stack).