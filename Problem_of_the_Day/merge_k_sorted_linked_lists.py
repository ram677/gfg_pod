#Merge K sorted linked lists

import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        min_heap = []
        
        # Push the head of each linked list into the min-heap
        for head in arr:
            if head:
                # Python's heapq works on tuples for custom sorting.
                # We store (node.data, node) to handle cases where two nodes have the same data.
                heapq.heappush(min_heap, (head.data, head))

        # Create a dummy node for the merged list
        dummy = Node(0)
        current = dummy
        
        # Build the merged list
        while min_heap:
            # Pop the smallest node from the heap
            data, min_node = heapq.heappop(min_heap)
            
            # Append it to the merged list
            current.next = min_node
            current = current.next
            
            # If the popped node has a next, push it to the heap
            if min_node.next:
                heapq.heappush(min_heap, (min_node.next.data, min_node.next))
                
        return dummy.next
    
#Time complexity: O(N log k)
#Space complexity: O(k)
#Where N is the total number of nodes in all linked lists and k is the number of linked lists.