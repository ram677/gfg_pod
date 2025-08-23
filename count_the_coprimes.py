#Count the Coprimes

class Solution:
    def cntCoprime(self, arr: list[int]) -> int:
        current_max_val = 0
        if arr:
            current_max_val = max(arr)
        
        MAX_VAL = current_max_val + 1 
        if MAX_VAL < 2:
            MAX_VAL = 2

        mu = [0] * MAX_VAL
        spf = [0] * MAX_VAL 
        primes = []

        mu[1] = 1 
        for i in range(2, MAX_VAL):
            if spf[i] == 0: 
                spf[i] = i
                primes.append(i)
                mu[i] = -1 
            
            for p in primes:
                if p > spf[i] or i * p >= MAX_VAL:
                    break
                
                spf[i * p] = p
                
                if p == spf[i]:
                    mu[i * p] = 0
                else: 
                    mu[i * p] = -mu[i]

        freq = [0] * MAX_VAL
        for x in arr:
            if x < MAX_VAL:
                freq[x] += 1

        multiples_count = [0] * MAX_VAL
        for g in range(1, MAX_VAL):
            for multiple_of_g in range(g, MAX_VAL, g):
                multiples_count[g] += freq[multiple_of_g]
        
        total_coprime_pairs = 0
        for g in range(1, MAX_VAL):
            count_g = multiples_count[g]
            P_g = (count_g * (count_g - 1)) // 2 

            total_coprime_pairs += mu[g] * P_g
        
        return total_coprime_pairs

#Time Complexity: O(n log n) where n is the maximum element in the array.
#Space Complexity: O(n) for the frequency and multiples_count arrays.