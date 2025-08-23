#Power of k in factorial of n

class Solution:
    def maxKPower(self, n, k):
        def prime_factors(k):
            factors = {}
            i = 2
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = 1
            return factors

        def count_p_in_factorial(n, p):
            count = 0
            div = p
            while div <= n:
                count += n // div
                div *= p
            return count

        k_factors = prime_factors(k)
        min_power = float('inf')

        for prime, required_power in k_factors.items():
            power_in_n_fact = count_p_in_factorial(n, prime)
            max_x = power_in_n_fact // required_power
            min_power = min(min_power, max_x)

        return min_power

#Time Complexity: O(n * log(k)) where n is the input number and k is the base.
#Space Complexity: O(log(k)) for the stack space used in prime factorization.