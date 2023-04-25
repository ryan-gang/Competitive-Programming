from heapq import heappush, heappop


# Runtime: 122 ms, faster than 72.53%.
# Memory Usage: 14.6 MB, less than 56.4%.
# T : O(M+N * LogN), S : O(N) ; M addBack() and N popSmallest() calls.
class SmallestInfiniteSet:
    """
    Our regular set of numbers can be emulated by just keeping an int
    `current_int` and incrementing it with each pop. For every addBack if the
    num is greater than the `current_int`, then no need to do anything, as it is
    not yet popped it is still present in the set, and we won't add it again.
    But, if the num is less than the `current_int` then we need to add it to our
    heap. AND TO NOTE HERE, THIS IS THE SMALLEST NUMBER NOW. It has to be, if it
    is larger than `current_int` we never store this. If heap has any members,
    we can directly pop them. But if the heap has a num, and we addBack the same
    num again, we need to skip that push, for this purpose we keep a set, of all
    currently backfilled nums, as we pop each of them from the heap we also
    remove them from the set, because in the future we might want to addBack
    them again.
    """

    def __init__(self):
        self.backfilled: set[int] = set()
        self.heap: list[int] = []
        self.current_int = 1

    def popSmallest(self) -> int:
        if self.heap:
            val = heappop(self.heap)
            self.backfilled.remove(val)
            return val
        self.current_int += 1
        return self.current_int - 1

    def addBack(self, num: int) -> None:
        if num not in self.backfilled and num < self.current_int:
            heappush(self.heap, num)
            self.backfilled.add(num)


if __name__ == "__main__":
    s = SmallestInfiniteSet()
    s.addBack(2)
    print(s.heap)
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.popSmallest())
    s.addBack(4)
    print(s.popSmallest())
    s.addBack(4)
    s.addBack(4)
    s.addBack(4)
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.popSmallest())
