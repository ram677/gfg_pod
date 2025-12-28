#Merge Sort for Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def get_middle(self, head):
        if not head:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

    def merge(self, list1, list2):
        dummy = Node(0)
        tail = dummy
        
        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next

    def mergeSort(self, head):
        # Base case
        if not head or not head.next:
            return head
            
        # 1. Divide the list into two halves
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # break the list into two halves
        
        # 2. Recursively sort the halves
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(next_to_middle)
        
        # 3. Merge the sorted halves
        sorted_head = self.merge(left_sorted, right_sorted)
        
        return sorted_head
    
#Time complexity: O(N log N)
#Space complexity: O(log N) for the recursion stack
#Where N is the number of nodes in the linked list.