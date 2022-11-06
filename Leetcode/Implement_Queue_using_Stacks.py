from collections import deque


# Runtime: 61 ms, faster than 28.21% of Python3 online submissions.
# Memory Usage: 14 MB, less than 75.37% of Python3 online submissions.
class MyQueue:
    """
    From CTCI.
    Logic is pretty clear, we keep on pushing into one stack.
    But for popping we need the reverse order, so we pop from here, and push to another
    stack, thus reversing the order. And giving us the required queue order.
    Then we pop from here. (At this point the prev stack is empty, cause we never pop from
    there, so its not an issue, we have the required elements in the 2nd stack anyway)
    We keep on pushing into that stack, but pop from here.
    If this stack becomes empty, after all the popping, we again copy over elements from that stack.
    """

    def __init__(self):
        self.head = deque()
        self.tail = deque()

    # T : O(1), S : O(N)
    def push(self, x: int) -> None:
        self.tail.append(x)

    # T : amortized O(1), S : O(1)
    # After copying N elements from tail, we can pop N elements from head.
    # 2N operations for N elements.
    # Amortized O(1) for each pop.
    def pop(self) -> int:
        self.carry_over()
        return self.head.pop()

    # T : amortized O(1), S : O(1)
    def peek(self) -> int:
        self.carry_over()
        return self.head[-1]

    def empty(self) -> bool:
        return not self.head and not self.tail

    def carry_over(self) -> None:
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())


if __name__ == "__main__":
    queue = MyQueue()
    for i in range(1, 10):
        queue.push(i)
    print(queue.empty())
    for i in range(1, 10):
        print(queue.peek(), queue.pop())
    print(queue.empty())
