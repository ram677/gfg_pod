#Median of BST

'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        
        # --- Helper function to count all nodes in the tree ---
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        # --- Helper function to find the k-th smallest element ---
        def find_kth(node):
            # Base case or if we've already found the median
            if not node or self.k_counter == 0:
                return

            # 1. Traverse the left subtree
            find_kth(node.left)

            # If the median was found in the left subtree, stop
            if self.k_counter == 0:
                return

            # 2. Visit the current node (the next smallest)
            self.k_counter -= 1
            if self.k_counter == 0:
                self.median_val = node.data
                return

            # 3. Traverse the right subtree
            find_kth(node.right)

        # Step 1: Count the total number of nodes
        n = count_nodes(root)

        # Step 2: Determine the position 'k' of the median
        if n % 2 == 0:
            k = n // 2
        else:
            k = (n + 1) // 2
        
        # We use instance variables to track state across recursive calls
        self.k_counter = k
        self.median_val = -1

        # Step 3: Perform an in-order traversal to find the k-th element
        find_kth(root)

        return self.median_val
    
# Time Complexity: O(N) where N is the number of nodes in the tree. In the worst case, we may need to visit all nodes.
# Space Complexity: O(H) due to the recursion stack in the worst case (unbalanced tree). In a balanced tree, the height H is log(N).