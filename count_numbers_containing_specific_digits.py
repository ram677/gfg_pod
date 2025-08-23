#Count Numbers Containing Specific Digits

class Solution:
    def countValid(self, n, arr):
        forbidden_digits = set(arr)

        total_n_digit_numbers = 9 * (10**(n - 1))

        count_first_digit_allowed = 0
        for digit in range(1, 10):
            if digit not in forbidden_digits:
                count_first_digit_allowed += 1
        
        count_other_digits_allowed = 0
        for digit in range(10):
            if digit not in forbidden_digits:
                count_other_digits_allowed += 1

        if count_first_digit_allowed == 0:
            numbers_without_forbidden = 0
        elif n == 1:
            numbers_without_forbidden = count_first_digit_allowed
        else:
            numbers_without_forbidden = count_first_digit_allowed * (count_other_digits_allowed**(n - 1))
        
        result = total_n_digit_numbers - numbers_without_forbidden
        
        return result

#Time Complexity: O(n) where n is the number of digits.
#Space Complexity: O(1) since we are using a constant amount of space.