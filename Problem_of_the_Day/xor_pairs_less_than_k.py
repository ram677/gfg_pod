#XOR Pairs less than K

class Solution:
    def cntPairs(self, arr, k):
        # Trie Node structure: [child_0, child_1, count]
        # Using a list for nodes is faster than a class in Python
        root = [None, None, 0]
        max_bits = 17 # sufficient for 5*10^4
        
        count = 0
        
        for num in arr:
            # 1. Query the Trie for pairs with 'num' < k
            node = root
            for i in range(max_bits - 1, -1, -1):
                if node is None:
                    break
                
                bit_n = (num >> i) & 1
                bit_k = (k >> i) & 1
                
                if bit_k == 1:
                    # If bit_k is 1, any number that results in XOR bit 0 
                    # makes the total XOR strictly less than k at this position.
                    # We want XOR result 0 -> we need a number with bit 'bit_n'.
                    if node[bit_n] is not None:
                        count += node[bit_n][2]
                    
                    # We then continue down the path where XOR result is 1 (matching k's bit)
                    # To get XOR 1 -> we need a number with bit '1 - bit_n'
                    node = node[1 - bit_n]
                else:
                    # If bit_k is 0, we MUST match it (XOR result 0) to stay potentially < k.
                    # If XOR result is 1, it would be > k, so we ignore that path.
                    # To get XOR 0 -> we need a number with bit 'bit_n'
                    node = node[bit_n]
            
            # 2. Insert 'num' into the Trie
            node = root
            node[2] += 1
            for i in range(max_bits - 1, -1, -1):
                bit = (num >> i) & 1
                if node[bit] is None:
                    # Create new node: [left, right, count]
                    node[bit] = [None, None, 0]
                node = node[bit]
                node[2] += 1
                
        return count
    
# Time Complexity: O(n * log(max_value)), where n is the length of the array and max_value is the maximum number in the array.
# Space Complexity: O(n * log(max_value)), for storing the Trie.