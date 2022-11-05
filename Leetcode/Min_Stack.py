from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass
class StackNode:
    value: int
    min_of_substack: int


# Runtime: 67 ms, faster than 88.87% of Python3 online submissions.
# Memory Usage: 20.1 MB, less than 6.15% of Python3 online submissions.
# T : O(1), S : O(N)
class MinStack:
    """
    From CTCI.
    We need to keep track of the min value in the substack uptil this point.
    And then we append this with the current node of the stack.
    So, at every node of the stack, we keep track of the value, and the min upto this point.
    If this node is popped, the next node still keeps track of the min upto that point.
    Very elegant solution. Without extra computation or space.
    """

    def __init__(self):
        self.stack: Deque[StackNode] = deque()

    def push(self, val: int) -> None:
        if self.stack:
            head = self.stack[-1]
            self.stack.append(StackNode(val, min(val, head.min_of_substack)))
        else:
            self.stack.append(StackNode(val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].min_of_substack


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
