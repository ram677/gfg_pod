#Implement UNDO & REDO

class Solution:
    def __init__(self):
        # Stores the current state of the document
        self.text = []
        # Stores characters popped by undo, allowing them to be restored
        self.redo_stack = []

    def append(self, x):
        # Append x into document
        self.text.append(x)
        # Standard behavior: A new action clears the redo history
        self.redo_stack = []

    def undo(self):
        # Undo last change: Remove from text and save to redo stack
        if self.text:
            char = self.text.pop()
            self.redo_stack.append(char)

    def redo(self):
        # Redo changes: Restore from redo stack back to text
        if self.redo_stack:
            char = self.redo_stack.pop()
            self.text.append(char)

    def read(self):
        # Read the document: Join list into a string
        return "".join(self.text)
    
# Time Complexity:
# - append: O(1)
# - undo: O(1)
# - redo: O(1)
# - read: O(N), where N is the length of the document.
# Space Complexity: O(N) for storing the document and redo stack.