#Divisible by 13

class Solution:
    def divby13(self, s):
        remainder = 0
        for digit in s:
            remainder = (remainder * 10 + int(digit)) % 13
        return remainder == 0

#Time Complexity: O(n) where n is the length of the string.
#Space Complexity: O(1) since we are using a constant amount of space.