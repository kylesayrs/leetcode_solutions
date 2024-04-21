from typing import Optional

import math


class Node:
    def __init__(self, value: int, minimum: int, prev: Optional["Node"]) -> None:
        self.value = value
        self.minimum = minimum
        self.prev = prev


class MinStack:
    def __init__(self):
        self.head = None


    def push(self, val: int) -> None:
        head_minimum = self.head.minimum if self.head is not None else math.inf
        self.head = Node(value=val, minimum=min(head_minimum, val), prev=self.head)
    

    def pop(self) -> None:
        if self.head is None:
            raise ValueError("Cannot `pop` empty MinStack")
        
        self.head = self.head.prev
        

    def top(self) -> int:
        if self.head is None:
            raise ValueError("Cannot `top` empty MinStack")
        
        return self.head.value
        

    def getMin(self) -> int:
        if self.head is None:
            raise ValueError("Cannot `getMin` of empty MinStack")
        
        return self.head.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
