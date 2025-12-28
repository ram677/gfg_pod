#ZigZag Tree Traversal

from collections import deque

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def zigZagTraversal(self, root):
        if not root:
            return []
            
        result = []
        queue = deque([root])
        left_to_right = True # Direction flag for traversal

        while queue:
            level_size = len(queue)
            # Use a deque for efficient appends to the front or back
            current_level_nodes = deque()

            for _ in range(level_size):
                node = queue.popleft()

                # Add node's value to the current level list based on direction
                if left_to_right:
                    current_level_nodes.append(node.data)
                else:
                    # For right-to-left, add to the front of the deque
                    current_level_nodes.appendleft(node.data)

                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the processed level to the final result
            result.extend(current_level_nodes)
            
            # Flip the direction for the next level
            left_to_right = not left_to_right
            
        return result
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(W) where W is the maximum width of the binary tree (due to the queue).