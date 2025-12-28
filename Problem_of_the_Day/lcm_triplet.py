#LCM Triplet

import math

class Solution:
    def lcmTriplets(self, n):
        # Base cases for small n
        if n == 1:
            return 1
        if n == 2:
            return 2 # LCM(1, 2)
        if n == 3:
            return 6 # LCM(1, 2, 3)

        # If n is odd, n, n-1, n-2 are pairwise coprime
        # n is odd implies n-1 is even, n-2 is odd.
        # GCD(n, n-1) = 1
        # GCD(n-1, n-2) = 1
        # GCD(n, n-2) = GCD(n-(n-2), n-2) = GCD(2, n-2) = 1 (since n-2 is odd)
        # So, n, n-1, n-2 are pairwise coprime.
        if n % 2 != 0:
            return n * (n - 1) * (n - 2)
        
        # If n is even
        # Check if n is a multiple of 3
        # If n is a multiple of 6 (n % 6 == 0), then n, n-2, n-3 are not good choices
        # because n and n-3 are both multiples of 3, and n and n-2 are both even.
        # Consider n-1, n-2, n-3
        # n-1 is odd
        # n-2 is even
        # n-3 is odd and multiple of 3
        # GCD(n-1, n-2) = 1
        # GCD(n-2, n-3) = 1
        # GCD(n-1, n-3) = GCD(n-1 - (n-3), n-3) = GCD(2, n-3) = 1 (since n-3 is odd)
        # So, n-1, n-2, n-3 are pairwise coprime.
        if n % 3 == 0:
            return (n - 1) * (n - 2) * (n - 3)
        
        # If n is even and not a multiple of 3 (n % 6 == 2 or n % 6 == 4)
        # Consider n, n-1, n-3
        # n is even
        # n-1 is odd
        # n-3 is odd
        # GCD(n, n-1) = 1
        # GCD(n-1, n-3) = GCD(n-1 - (n-3), n-3) = GCD(2, n-3) = 1 (since n-3 is odd)
        # GCD(n, n-3) = GCD(n - (n-3), n-3) = GCD(3, n-3) = 1 (since n is not a multiple of 3)
        # So, n, n-1, n-3 are pairwise coprime.
        return n * (n - 1) * (n - 3)

#Time Complexity: O(1) since we are only doing a constant amount of work.
#Space Complexity: O(1) since we are using a constant amount of space.