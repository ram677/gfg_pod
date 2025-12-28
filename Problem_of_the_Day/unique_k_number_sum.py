#Unique K-Number Sum

from typing import List

class Solution:
    def combinationSum(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        # Backtracking helper function
        def backtrack(remaining_sum: int, k_left: int, start_num: int, current_combo: List[int]):
            # Base Case: A valid combination is found
            if remaining_sum == 0 and k_left == 0:
                # Add a copy of the combination to the result list
                result.append(list(current_combo))
                return

            # Pruning Cases: If the path is no longer viable, stop.
            if remaining_sum < 0 or k_left == 0:
                return

            # Iterate through the candidate numbers (from 1 to 9)
            for i in range(start_num, 10):
                # --- Choose ---
                current_combo.append(i)
                
                # --- Explore ---
                # Recurse with updated state. The next number must be > i.
                backtrack(remaining_sum - i, k_left - 1, i + 1, current_combo)
                
                # --- Unchoose (Backtrack) ---
                current_combo.pop()

        # Start the backtracking process
        backtrack(n, k, 1, [])
        return result
    
# Time Complexity: O(9 choose k) in the worst case, where k is the number of elements to choose.
# Space Complexity: O(k) for the recursion stack and the space used to store the combinations in the result.