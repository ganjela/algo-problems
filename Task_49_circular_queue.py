"""
CircularQueue is implemented using list where each function runs in O(1) time.

Only hard part of this problem was to come up with the idea of how to wrap around start and end
pointers meaning, using the modulo operator:
enQueue - self.end = (self.end + 1) % self.k
deQueue - self.start = (self.start + 1) % self.k

This lines make sure that when pointers reach to end of the list they wrap around. This avoids
index out of range error and makes use of free space in the list.
"""

class CircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.k = k
        self.start = 0
        self.end = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.end] = value
        self.size += 1
        self.end = (self.end + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.start = (self.start + 1) % self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.end-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k