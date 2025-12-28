#Subset XOR

class Solution:
    def subsetXOR(self, n: int):
        # 1. Calculate the XOR sum of all numbers from 1 to n
        rem = n % 4
        if rem == 0:
            X = n
        elif rem == 1:
            X = 1
        elif rem == 2:
            X = n + 1
        else: # rem == 3
            X = 0
            
        # 2. Calculate the value 'R' that needs to be removed
        # We need (X ^ R) = n, therefore R = X ^ n
        R = X ^ n
        
        # 3. Build the subset
        # We include all numbers from 1 to n, skipping only R (if R > 0)
        res = []
        for i in range(1, n + 1):
            if i == R:
                continue
            res.append(i)
            
        return res
    
# Time Complexity: O(n), where n is the input number.
# Space Complexity: O(n), for storing the result subset.