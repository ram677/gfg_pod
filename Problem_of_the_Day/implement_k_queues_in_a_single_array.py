#Implement k Queues in a Single Array

class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * n          # Stores actual data
        self.front = [-1] * k       # Stores front index for each queue
        self.rear = [-1] * k        # Stores rear index for each queue
        self.next = [i + 1 for i in range(n)] # Stores next pointers
        self.next[n - 1] = -1       # End of free list
        self.free = 0               # Start of free list
        
    def enqueue(self, x, i):
        # Check if array is full
        if self.isFull():
            return False
            
        # 1. Get the first free slot index
        index = self.free
        
        # 2. Update free to the next available slot
        self.free = self.next[index]
        
        # 3. If queue is empty, update front; else link new slot to current rear
        if self.isEmpty(i):
            self.front[i] = index
        else:
            self.next[self.rear[i]] = index
            
        # 4. Update next of new slot to -1 (end of queue)
        self.next[index] = -1
        
        # 5. Update rear to the new slot and store value
        self.rear[i] = index
        self.arr[index] = x
        return True

    def dequeue(self, i):
        # Check if queue is empty
        if self.isEmpty(i):
            return -1
            
        # 1. Get the index of the front element
        index = self.front[i]
        
        # 2. Move front to the next element in the queue
        self.front[i] = self.next[index]
        
        # 3. Add the freed slot back to the free list
        self.next[index] = self.free
        self.free = index
        
        return self.arr[index]

    def isEmpty(self, i):
        return self.front[i] == -1
        
    def isFull(self):
        return self.free == -1
    
# Time Complexity:
# Enqueue and Dequeue operations take O(1) time.
# Space Complexity:
# O(n) space is used for the array and auxiliary structures.    

