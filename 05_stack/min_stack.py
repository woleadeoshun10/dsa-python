"""
Problem: Min Stack
Pattern: Stack
Difficulty: Medium

Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

Approach:
Use two stacks:
1. mainStack → stores all values
2. minStack → stores the current minimum values

Time Complexity:
push  → O(1)
pop   → O(1)
top   → O(1)
getMin → O(1)

Space Complexity: O(n)
"""

class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.mainStack.pop()

        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]