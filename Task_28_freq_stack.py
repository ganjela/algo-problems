from collections import defaultdict

"""
Frequency stack keeps track of current maximum frequency and frequency values for each element.

Also, we have seperated each frequencies into different stacks. Which will ensure that elements 
with same frequency are popped in order with time complexity O(1).
"""

class FreqStack:
    def __init__(self):
        self.stacks = defaultdict(list)
        self.value_frequency = defaultdict(int)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        new_frequency = self.value_frequency[val] + 1
        if new_frequency > self.max_frequency:
            self.max_frequency = new_frequency
        self.value_frequency[val] = new_frequency
        self.stacks[new_frequency].append(val)

    def pop(self) -> int:
        most_freq = self.stacks[self.max_frequency].pop()
        self.value_frequency[most_freq] -= 1
        if not self.stacks[self.max_frequency]:
            self.max_frequency -= 1
        return most_freq