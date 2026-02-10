#Missing and Repeating in an Array

#-----------------------------------------------------------------------------------------------------------
#APPROACH 1: Using Visited Array
#-----------------------------------------------------------------------------------------------------------
"""
The idea is to use a frequency array to keep track of how many times each number appears in the original array. 
Since we know the numbers should range from 1 to n with each appearing exactly once, any number appearing twice is our repeating number, and any number with zero frequency is our missing number.
"""

def findTwoElement1(arr):
    n = len(arr)

    # frequency array to count occurrences
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    # count frequency of each element
    for num in arr:
        freq[num] += 1

    # identify missing and repeating numbers
    for i in range(1, n + 1):
        if freq[i] == 0:
            missing = i
        elif freq[i] == 2:
            repeating = i

    return [repeating, missing]

# if __name__ == "__main__":
#     arr = [3, 1, 3]
#     ans = findTwoElement(arr)
#     print(ans[0], ans[1])

# Time Complexity: O(n) where n is the length of the input array, due to the single pass to count frequencies and another pass to identify missing and repeating numbers.
# Space Complexity: O(n) due to the additional frequency array used to count occurrences of each number.

#--------------------------------------------------------------------------------------------------------------------------
#APPROACH 2: Using Array Marking
#--------------------------------------------------------------------------------------------------------------------------
"""
The main idea is to use the input array itself for tracking: it negates the value at the index corresponding to each element to mark it as visited. 
If it encounters a value that has already been negated, it identifies that number as the repeating one. 
In a second pass, it finds the index that remains positive, which corresponds to the missing number. 
"""

def findTwoElement2(arr):
    n = len(arr)
    repeating = -1

    # mark visited indices by negating the value 
    # at that index
    for i in range(n):
        val = abs(arr[i])

        # if value at index val - 1 is already negative,
        # val is repeating
        if arr[val - 1] > 0:
            arr[val - 1] = -arr[val - 1] 
        else:
            # Already visited → repeating element
            repeating = val  

    missing = -1

    # the index with a positive value corresponds 
    # to the missing number
    for i in range(n):
        if arr[i] > 0:
            missing = i + 1
            break

    return [repeating, missing]

# Time Complexity: O(n) where n is the length of the input array, due to the two passes through the array.
# Space Complexity: O(1) as we are using only constant extra space for variables, and we are modifying the input array in place without using any additional data structures.

#--------------------------------------------------------------------------------------------------------------------------
# APPROACH 3: Making Two Math Equations
#--------------------------------------------------------------------------------------------------------------------------
"""
The idea is to use mathematical equations based on the sum and sum of squares of numbers from 1 to n. 
The difference between expected and actual sums will give us one equation, and the difference between expected and actual sum of squares will give us another equation. 
Solving these equations yields our missing and repeating numbers.
"""
def findTwoElement(arr):
    n = len(arr)

    # Expected sum and sum of squares for numbers from 1 to n
    s = (n * (n + 1)) // 2
    ssq = (n * (n + 1) * (2 * n + 1)) // 6

    missing = 0
    repeating = 0

    # Subtract actual sum and sum of squares from expected values
    for num in arr:
        s -= num
        ssq -= num * num

    # Let s = x - y and ssq = x^2 - y^2 = (x - y)(x + y)
    # => x = (s + ssq // s) // 2, y = x - s
    missing = (s + ssq // s) // 2
    repeating = missing - s

    return [repeating, missing]

# Time Complexity: O(n) where n is the length of the input array, due to the single pass to calculate sums and sum of squares.
# Space Complexity: O(1) as we are using only constant extra space for variables.


if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1])