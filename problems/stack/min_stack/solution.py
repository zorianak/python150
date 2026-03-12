from typing import List, Optional

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min = float('inf')
        pass

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop 

    def top(self) -> int:
        pop = self.stack[-1]
        if pop > 0:
            return pop + self.min
        else:
            return self.min
        pass

    def getMin(self) -> int:
        return self.min
