#Minimum sum

class Solution:
    def minSum(self, arr):
        arr.sort()
        num1 = []
        num2 = []

        # Distribute digits alternately
        for i in range(len(arr)):
            if i % 2 == 0:
                num1.append(str(arr[i]))
            else:
                num2.append(str(arr[i]))

        # Perform string-based addition
        def addStrings(a, b):
            i, j = len(a) - 1, len(b) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0 or carry:
                digit1 = int(a[i]) if i >= 0 else 0
                digit2 = int(b[j]) if j >= 0 else 0
                total = digit1 + digit2 + carry
                res.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(res[::-1])

        return addStrings(''.join(num1), ''.join(num2)).lstrip('0') or '0'

#Time Complexity: O(n log n) where n is the number of elements in the array
#Space Complexity: O(n) for the sorted lists