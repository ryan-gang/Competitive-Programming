from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Pop 2 biggest stones from heap, push the difference back in.
        """
        if len(stones) > 1:
            stones = [-s for s in stones]
            heapify(stones)

        while len(stones) > 1:
            biggest, bigger = -heappop(stones), -heappop(stones)
            big = biggest - bigger
            if big:
                heappush(stones, -big)

        return abs(stones[0]) if stones else 0

    def lastStoneWeight1(self, stones: list[int]):
        h = [-x for x in stones]
        heapify(h)
        while len(h) > 1 and h[0] != 0:
            heappush(h, heappop(h) - heappop(h))
        return -h[0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.lastStoneWeight(stones=[2, 2]) == 0
    assert sol.lastStoneWeight(stones=[3, 7, 2]) == 2
    assert sol.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight(stones=[1]) == 1
