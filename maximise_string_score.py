#Maximise String Score

class Solution:
    def maxScore(self, s, jumps):
        n = len(s)
        
        # 1. Parse Jumps
        allowed_sources = {chr(i): [] for i in range(97, 123)} 
        for u, v in jumps:
            allowed_sources[v].append(u)
            
        unique_chars = set(s)
        for c in unique_chars:
            if c not in allowed_sources[c]:
                allowed_sources[c].append(c)

        # 2. State Management
        # best_metric[source_char][target_char] stores:
        # max(dp[i] - P[i] + C[i][target] * target_val)
        best_metric = {} 
        for c in unique_chars:
            best_metric[c] = {}
            for target in unique_chars:
                best_metric[c][target] = -float('inf')

        # 3. Iteration variables
        # P[x]: Sum of ASCII values s[0]...s[x-1]
        # At start of loop j, current_prefix_sum represents P[j]
        current_prefix_sum = 0
        
        # C[x][char]: Count of char in s[0]...s[x-1]
        # At start of loop j, char_counts represents C[j]
        char_counts = {c: 0 for c in unique_chars}
        
        # Initialize for index 0
        # dp[0] = 0.
        # We need to compute the metric for index 0 acting as a source 'i=0'.
        # metric = dp[0] - P[0] + C[0][target] * target_val
        # P[0] = 0, C[0] = 0. So metric = 0.
        
        start_char = s[0]
        # Update metrics for i=0
        for target in unique_chars:
            target_val = ord(target)
            # metric = 0 - 0 + 0 * target_val = 0
            best_metric[start_char][target] = 0

        # Before entering loop for j=1, update running sums to include s[0]
        current_prefix_sum += ord(start_char)
        char_counts[start_char] += 1
        
        max_score = 0
        
        for j in range(1, n):
            u = s[j] # This is s[j]
            u_val = ord(u)
            
            # --- Step A: Calculate dp[j] ---
            # dp[j] = P[j] - C[j][u]*u_val + max_metric
            current_dp = -float('inf')
            
            # Try coming from any valid source character 'v'
            for v in allowed_sources[u]:
                if v in best_metric:
                    prev_metric = best_metric[v][u]
                    if prev_metric == -float('inf'):
                        continue
                        
                    # Apply formula: P[j] is current_prefix_sum, C[j][u] is char_counts[u]
                    score = prev_metric + current_prefix_sum - (char_counts[u] * u_val)
                    if score > current_dp:
                        current_dp = score
            
            if current_dp > max_score:
                max_score = current_dp
            
            # --- Step B: Update State for i = j ---
            # Now index 'j' becomes a potential 'i' for future jumps.
            # We need to compute metric for this new 'i':
            # new_metric = dp[j] - P[j] + C[j][target] * target_val
            
            if current_dp != -float('inf'):
                if u in best_metric:
                    for target in unique_chars:
                        target_val = ord(target)
                        val = current_dp - current_prefix_sum + (char_counts[target] * target_val)
                        if val > best_metric[u][target]:
                            best_metric[u][target] = val
                            
            # --- Step C: Update Prefix Sums/Counts for next iteration ---
            current_prefix_sum += u_val
            char_counts[u] += 1
                            
        return max_score

# Time Complexity: O(n * m), where n is the length of the string and m is the number of unique characters.
# Space Complexity: O(m^2), for storing the best_metric dictionary.