#Symmetric Tree

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
            
        if not left or not right:
            return False
        
        return (left.data == right.data and 
                self.isMirror(left.left, right.right) and 
                self.isMirror(left.right, right.left))

#Time Complexity: O(n) where n is the number of nodes in the tree
#Space Complexity: O(h) where h is the height of the tree (for the recursion stack)