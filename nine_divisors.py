#Nine Divisors

class Solution:
    def countNumbers(self, n):
        import math

        # Sieve of Eratosthenes up to sqrt(n)
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(math.sqrt(limit)) + 1):
                if is_prime[i]:
                    for j in range(i*i, limit + 1, i):
                        is_prime[j] = False
            return [i for i, prime in enumerate(is_prime) if prime]

        limit = int(n ** 0.5) + 1
        primes = sieve(limit)

        count = 0

        # Case 1: p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        # Case 2: p1^2 * p2^2
        length = len(primes)
        for i in range(length):
            for j in range(i + 1, length):
                if primes[i]**2 * primes[j]**2 <= n:
                    count += 1
                else:
                    break

        return count

#Time Complexity: O(n * log(log(n))) for the Sieve of Eratosthenes and O(1) for the counting.
#Space Complexity: O(sqrt(n)) for the list of primes.