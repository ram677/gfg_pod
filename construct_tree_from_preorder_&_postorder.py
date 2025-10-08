#Construct Tree from Preorder & Postorder

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructTree(self, pre, post):
        # A map for O(1) lookup of a value's index in the postorder array.
        post_map = {val: i for i, val in enumerate(post)}
        
        # A recursive helper function that builds the tree using indices.
        def build(pre_start, pre_end, post_start, post_end):
            # Base Case 1: If the current subarray is empty.
            if pre_start > pre_end:
                return None
            
            # The first element of the preorder subarray is the root of the current tree.
            root = Node(pre[pre_start])
            
            # Base Case 2: If there's only one element, it's a leaf node.
            if pre_start == pre_end:
                return root
            
            # The next element in preorder is the root of the left subtree.
            left_subtree_root_val = pre[pre_start + 1]
            
            # Find the index of the left subtree's root in the postorder array.
            post_idx_of_left_root = post_map[left_subtree_root_val]
            
            # Calculate how many nodes are in the left subtree.
            num_nodes_in_left = (post_idx_of_left_root - post_start) + 1
            
            # Recursively build the left subtree using the calculated boundaries.
            root.left = build(
                pre_start + 1, 
                pre_start + num_nodes_in_left, 
                post_start, 
                post_idx_of_left_root
            )
            
            # Recursively build the right subtree.
            root.right = build(
                pre_start + num_nodes_in_left + 1, 
                pre_end, 
                post_idx_of_left_root + 1, 
                post_end - 1
            )
                               
            return root

        # Start the construction with the full arrays.
        n = len(pre)
        return build(0, n - 1, 0, n - 1)
    
# Time Complexity: O(N) where N is the number of nodes. Each node is processed once.
# Space Complexity: O(N) for the recursion stack and the post_map.