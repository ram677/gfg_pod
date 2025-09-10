#Largest number in one swap

class Solution:
    def largestSwap(self, s):
        s_list = list(s)
        n = len(s_list)
        
        for i in range(n):
            # Find the largest digit to the right of s_list[i]
            max_digit = s_list[i]
            max_idx = i
            for j in range(i + 1, n):
                if s_list[j] >= max_digit:
                    max_digit = s_list[j]
                    max_idx = j
            
            # If a larger digit is found, perform the swap
            if max_digit > s_list[i]:
                # Find the rightmost occurrence of the max_digit
                rightmost_max_idx = max_idx
                for k in range(max_idx + 1, n):
                    if s_list[k] == max_digit:
                        rightmost_max_idx = k

                s_list[i], s_list[rightmost_max_idx] = s_list[rightmost_max_idx], s_list[i]
                return "".join(s_list)
        
        return s

#Time Complexity: O(n^2) in the worst case due to nested loops
#Space Complexity: O(n) for the list conversion
#Where n is the length of the input string s.