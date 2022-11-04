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


class MedianFinderWrong:
    """
    Because of less feedback from small, both heaps go out of sorted order very fast.
    Need to pop from small and push to large also sometimes.
    """

    def __init__(self):
        self.small = []  # max_heap
        self.large = []  # min_heap

    def addNum(self, num):
        heappush(self.large, num)
        if len(self.large) - len(self.small) > 1:
            heappush(self.small, -heappop(self.large))

    def findMedian(self):
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (self.large[0] - self.small[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    # for i in [10, 13, 7, 9, 8, 11, 12, 14]:
    for i in [-1, -2, -3, -4, -5]:
        mf.addNum(i)
        print(mf.small, mf.large, mf.findMedian())
