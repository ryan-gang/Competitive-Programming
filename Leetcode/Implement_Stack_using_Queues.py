from collections import deque


class MyStack:
    """
    This solution achieves push in O(1) time and pop in O(N) time.
    We can also handle the entire FIFO to LIFO thing in the push phase, where we can pop and push
    all the values into the secondary deque to achieve the proper ordering.
    This can be done using a separate secondary array or even the same array.
    In this scenario Push becomes O(N) and pop becomes O(1).
    """
    def __init__(self):
        self.primary: deque[int] = deque()
        self.secondary: deque[int] = deque()
        self.length = 0
        self._top = -1

    def push(self, x: int) -> None:
        self.primary.append(x)
        self._top = x
        self.length += 1

    def pop(self) -> int:
        for _ in range(self.length - 1):
            self._top = self.primary.popleft()
            self.secondary.append(self._top)
        val = self.primary.popleft()
        self.primary = self.secondary
        self.secondary = deque()
        self.length -= 1
        return val

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return self.length == 0
