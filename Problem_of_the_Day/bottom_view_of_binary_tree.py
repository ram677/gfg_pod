#Bottom View of Binary Tree

from collections import deque

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        if not root:
            return []
            
        # A map to store the last seen node for each horizontal distance.
        # Format: {horizontal_distance: node_data}
        view_map = {}
        
        # Queue for level-order traversal, storing (node, horizontal_distance).
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # As we traverse down the tree, we update the node for the current
            # horizontal distance. The last one seen will be the bottom-most.
            view_map[hd] = node.data
            
            # Add children to the queue with their respective horizontal distances.
            if node.left:
                queue.append((node.left, hd - 1))
            
            if node.right:
                queue.append((node.right, hd + 1))
                
        # The map now contains the bottom view, but the keys are not ordered.
        # Sort the map by keys (horizontal distance) to get the final view.
        sorted_keys = sorted(view_map.keys())
        
        # Build the result list from the sorted map.
        result = [view_map[key] for key in sorted_keys]
        
        return result
    
# Time Complexity: O(N log N) due to sorting the horizontal distances, where N is the number of nodes in the tree.
# Space Complexity: O(N) for the queue and the view_map in the worst case.