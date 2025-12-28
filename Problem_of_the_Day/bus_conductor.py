#Bus Conductor

class Solution:
    def findMoves(self, chairs, passengers):
        # Sort both arrays to align the closest passenger-chair pairs greedily
        chairs.sort()
        passengers.sort()
        
        total_moves = 0
        n = len(chairs)
        
        # Calculate the distance for each pair
        for i in range(n):
            total_moves += abs(chairs[i] - passengers[i])
            
        return total_moves
    
# Time Complexity: O(n log n) due to sorting, where n is the number of chairs/passengers.
# Space Complexity: O(1) if we ignore the input storage, as we are sorting in place.