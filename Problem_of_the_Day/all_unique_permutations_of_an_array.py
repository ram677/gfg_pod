#All Unique Permutations of an array

from typing import List

class Solution:
    def uniquePerms(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        result = []
        
        # Sort the array to handle duplicates efficiently.
        arr.sort()
        
        # 'used' array tracks which elements are in the current permutation.
        used = [False] * n

        def backtrack(current_permutation: List[int]):
            # Base case: A full permutation has been formed.
            if len(current_permutation) == n:
                # Add a copy of the completed permutation to the result.
                result.append(list(current_permutation))
                return

            for i in range(n):
                # If the element is already used in the current path, skip it.
                if used[i]:
                    continue
                
                # The core rule to prevent duplicate permutations:
                # If the current element is the same as the previous one,
                # AND the previous one has not been used, skip this element.
                if i > 0 and arr[i] == arr[i-1] and not used[i-1]:
                    continue

                # --- Choose ---
                used[i] = True
                current_permutation.append(arr[i])
                
                # --- Explore ---
                backtrack(current_permutation)
                
                # --- Unchoose (Backtrack) ---
                current_permutation.pop()
                used[i] = False

        backtrack([])
        return result
    
# Time Complexity: O(n * n!) in the worst case, where n is the length of the array.
# Space Complexity: O(n) for the recursion stack and the space used to store the permutations