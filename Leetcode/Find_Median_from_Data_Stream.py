from heapq import heappush, heappushpop, heappop


class MedianFinder:
    # Runtime: 1253 ms, faster than 57.50% of Python3 online submissions.
    # Memory Usage: 36 MB, less than 65.88% of Python3 online submissions.
    # T : O(NlogK), S : O(N)
    def __init__(self):
        self.small = []  # max_heap
        self.large = []  # min_heap

    def addNum(self, num):
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    def findMedian(self):
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (self.large[0] - self.small[0]) / 2.0


# Runtime: 539 ms, faster than 96.47% of Python3 online submissions.
# Memory Usage: 36.1 MB, less than 57.44% of Python3 online submissions.
class MedianFinder2:
    def __init__(self):
        self.small = []  # max_heap
        self.large = []  # min_heap

    def addNum(self, num):
        smallest = heappushpop(self.large, num)
        heappush(self.small, -smallest)
        if len(self.small) - len(self.large) > 1:
            largest = -heappop(self.small)
            heappush(self.large, largest)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -float(self.small[0])
        return (self.large[0] - self.small[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    # for i in [10, 13, 7, 9, 8, 11, 12, 14]:
    for i in [-1, -2, -3, -4, -5]:
        mf.addNum(i)
        print(mf.small, mf.large, mf.findMedian())
