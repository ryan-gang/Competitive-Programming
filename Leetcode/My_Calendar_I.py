from StarterCode.binary_tree import prettyPrintTree


# Runtime: 4268 ms, faster than 5.01% of Python3 online submissions.
# Memory Usage: 14.7 MB, less than 58.88% of Python3 online submissions.
class MyCalendarNaive:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        overlap = False
        for item in self.calendar:
            if max(start, item[0]) < min(end, item[1]):
                overlap = True
        if not overlap:
            self.calendar.append([start, end])
        return not overlap


class Node(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.val = f"{self.start}:{self.end}"

    def insert(self, start, end):
        if start >= self.end:
            if self.right:
                return self.right.insert(start, end)
            else:
                self.right = Node(start, end)
                return True
        elif end <= self.start:
            if self.left:
                return self.left.insert(start, end)
            else:
                self.left = Node(start, end)
                return True
        else:
            return False


# Runtime: 251 ms, faster than 93.52% of Python3 online submissions.
# Memory Usage: 14.7 MB, less than 92.29% of Python3 online submissions.
class MyCalendar(object):
    def __init__(self) -> None:
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(start, end)


if __name__ == "__main__":
    obj = MyCalendar()
    for item in [
        [47, 50],
        [33, 41],
        [39, 45],
        [33, 42],
        [25, 32],
        [26, 35],
        [19, 25],
        [3, 8],
        [8, 13],
        [18, 27],
    ]:
        print(f"{item}: {obj.book(item[0], item[1])}")

    prettyPrintTree(obj.root)
