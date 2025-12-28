#Postorder Traversal

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        result = []
        
        def traverse(node):
            # Base case: do nothing if the node is null
            if not node:
                return
            
            # 1. Traverse the left subtree
            traverse(node.left)
            
            # 2. Traverse the right subtree
            traverse(node.right)
            
            # 3. Visit the root node
            result.append(node.data)
            
        traverse(root)
        return result
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(H) where H is the height of the binary tree (due to recursion stack).