from collections import deque
from heapq import heappop, heappush
from typing import List


# Ref : problems/dinner-plate-stacks/discuss/366331/C%2B%2BPython-Two-Solutions
# Runtime: 994 ms, faster than 88.00% of Python3 online submissions.
# Memory Usage: 154.4 MB, less than 5.00% of Python3 online submissions.
# Push : O(logN)
# Pop : amortized O(1) (More info @ bottom)
# PopAtStack : O(log N)
class DinnerPlates:
    def __init__(self, capacity: int):
        self.stacks = [deque()]
        self.max_capacity = capacity
        # push_where is a min_heap keeping track of indices in the stacks array,
        # which might have empty spaces. We fetch the min index, and see if
        # an empty space is there or not, if not fetch next, until its empty.
        # At which point create a new stack and add index to heap.
        self.push_where: List[int] = []
        heappush(self.push_where, 0)  # idx of stack in stacks with empty space

    def push(self, val: int) -> None:
        # Get the most left stack, with an empty place.
        # Until then we keep on popping from our heap.
        # We pop if stack has reached max_capacity or
        # if index is greater than our current len of stacks. (Prev valid stack but popped off)
        while (
            self.push_where
            and self.push_where[0] < len(self.stacks)
            and len(self.stacks[self.push_where[0]]) == self.max_capacity
        ):
            heappop(self.push_where)

        # If no stacks present, with an empty place.
        # We create a new stack, and then add this index to our heap.
        if not self.push_where or self.push_where[0] == len(self.stacks):
            self.stacks.append(deque())
            new_idx = len(self.stacks) - 1
            heappush(self.push_where, new_idx)

        # Guaranteed to be valid.
        # We can add the element in this stack.
        # If stack is still empty, add it's index to heap.
        idx = heappop(self.push_where)
        used_capacity = len(self.stacks[idx])
        stack = self.stacks[idx]

        stack.append(val)
        used_capacity += 1

        if used_capacity < self.max_capacity:
            heappush(self.push_where, idx)

    def pop(self) -> int:
        # Pop off all the tail stacks, that are empty. Saves space.
        while self.stacks and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        # This index should have atleast one element,
        # or will be < 0, in that case no stacks present.
        idx = len(self.stacks) - 1
        return self.popAtStack(idx)

    def popAtStack(self, index: int) -> int:
        # If no stacks present, or index is out of range (>len(stacks))
        # Or if the stack at this index is empty, return -1
        # Else pop.
        # And as we are creating a new empty space, add index to heap.
        if index < 0 or index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1
        stack = self.stacks[index]
        heappush(self.push_where, index)
        return stack.pop()


if __name__ == "__main__":
    ####################################################
    # Test 1
    # obj = DinnerPlates(capacity=2)
    # for i in range(1, 6):
    #     obj.push(i)
    # print(obj.stacks)
    # print(obj.pop())
    # print(obj.stacks)
    # print(obj.pop())
    # print(obj.stacks)

    # for i in range(6, 10):
    #     obj.push(i)

    # print(obj.stacks)
    # print(obj.popAtStack(2))
    # print(obj.popAtStack(1))
    # print(obj.popAtStack(3))
    # print(obj.popAtStack(0))
    # print(obj.stacks)

    # print(obj.pop())
    # print(obj.stacks)

    # for i in range(21, 25):
    #     obj.push(i)

    # print(obj.stacks)
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.stacks)
    ####################################################
    # Test 2
    # obj = DinnerPlates(capacity=2)
    # for i in range(1, 6):
    #     obj.push(i)
    # print(obj.stacks)
    # print(obj.popAtStack(0))
    # print(obj.stacks)
    # obj.push(20)
    # obj.push(21)
    # print(obj.stacks)
    # print(obj.popAtStack(0))
    # print(obj.popAtStack(2))
    # print(obj.stacks)
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.stacks)
    ####################################################
    A = [
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "popAtStack",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "pop",
        "pop",
        "pop",
        "pop",
        "pop",
        "pop",
        "pop",
        "pop",
        "pop",
        "pop",
    ]
    B = [
        [472],
        [106],
        [497],
        [498],
        [73],
        [115],
        [437],
        [461],
        [3],
        [3],
        [1],
        [3],
        [0],
        [2],
        [2],
        [1],
        [1],
        [3],
        [197],
        [239],
        [129],
        [449],
        [460],
        [240],
        [386],
        [343],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    m = globals()["DinnerPlates"](capacity=2)

    try:
        for i, j in zip(A, B):
            print(i, j)
            func = getattr(m, i)
            func(j[0])
    except Exception:
        print(m.stacks)

"""Why Pop is amortized O(1) ?
heappush() is O(logN), but this is only when you add A RANDOM ELEMENT. Here we are always pushing
the GREATEST ELEMENT. Note how popAtStack is called with A RANDOM ELEMENT and but pop calls
heappush always with the GREATEST ELEMENT in the stack.

1. An element is added at the end of the array that is underlying the implementation of the heap.
2. Then a relaxation step begins: while this element is smaller than it's parent, it is switched
with it's parent.

In this case it's obvious that the step 2 instead of being logN will only be O(1).

This is similar to adding an element to a sorted array:
Complexity for a random element: O(N)
Complexity for adding an element greater than the max in the array O(1)"""
