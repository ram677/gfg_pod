#Maximum Stone Removal

class Solution:
    def maxRemove(self, stones):
        parent = {}

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function to merge two sets
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Process each stone
        for r, c in stones:
            # To distinguish row coordinates from column coordinates,
            # we can map column 'c' to a unique identifier like 'c + 10001'
            # (since coordinates are <= 10000).
            # However, using a string prefix or similar trick works too,
            # or simply ~c (bitwise NOT) which maps 0 to -1, 1 to -2, etc.
            row_id = r
            col_id = ~c  # Unique ID for columns distinct from rows
            
            if row_id not in parent: parent[row_id] = row_id
            if col_id not in parent: parent[col_id] = col_id
            
            union(row_id, col_id)

        # Count the number of unique connected components
        # A component is identified by its unique root in the parent map
        unique_roots = set()
        for r, c in stones:
            unique_roots.add(find(r))
            
        # Total stones - number of connected components
        return len(stones) - len(unique_roots)
    
# Time Complexity: O(N * α(N)) where N is the number of stones and α is the inverse Ackermann function.
# Space Complexity: O(N) for the parent dictionary.