import heapq
from typing import List


class Solution:
    # Runtime: 1809 ms, faster than 93.31%.
    # Memory Usage: 28.6 MB, less than 44.43%.
    # T : O(N + KLogN), S : O(N)
    # O(N) for heapify, and K times O(logN) insertion.
    # Heapify time complexity : https://stackoverflow.com/questions/51735692/
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        while k > 0:
            stone = -heapq.heappop(piles)
            stone -= stone // 2
            heapq.heappush(piles, -stone)
            k -= 1
            # Can be replaced by a single line :
            # heapq.heapreplace(piles, piles[0] / 2)
        return -sum(piles)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minStoneSum(piles=[5, 4, 9], k=2) == 12
    assert sol.minStoneSum(piles=[4, 3, 6, 7], k=3) == 12
