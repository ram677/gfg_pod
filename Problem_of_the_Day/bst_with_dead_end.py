#BST with Dead End

class Solution:
    def isDeadEnd(self, root):

        if not root:
            return False
        
        # Store all values in the BST for O(1) lookup
        all_values = set()
        
        def collect_values(node):
            """Collect all node values in the BST"""
            if node:
                all_values.add(node.data)
                collect_values(node.left)
                collect_values(node.right)
        
        def check_dead_ends(node):
            """Check if any leaf node is a dead end"""
            if not node:
                return False
            
            # If it's a leaf node, check dead end condition
            if not node.left and not node.right:
                x = node.data
                
                # Check if x-1 is blocked (either x=1 or x-1 exists)
                left_blocked = (x == 1) or ((x - 1) in all_values)
                
                # Check if x+1 is blocked (exists in BST)
                right_blocked = (x + 1) in all_values
                
                # Dead end if both directions are blocked
                if left_blocked and right_blocked:
                    return True
            
            # Recursively check left and right subtrees
            return check_dead_ends(node.left) or check_dead_ends(node.right)
        
        # First pass: collect all values
        collect_values(root)
        
        # Second pass: check for dead ends
        return check_dead_ends(root)

#Time Complexity: O(n) where n is the number of nodes in the BST
#Space Complexity: O(n) for the set storing all node values.