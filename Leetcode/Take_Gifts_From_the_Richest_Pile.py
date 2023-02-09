from heapq import heapify, heappop, heappush
from math import sqrt


class Solution:
    # Runtime: 47 ms, faster than 85.33%.
    # Memory Usage: 13.9 MB, less than 99%.
    # T : O(N + KLogN), S : O(N)
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapify(gifts)

        while k > 0:
            val = -heappop(gifts)
            keep = int(sqrt(val))
            heappush(gifts, -keep)

            k -= 1

        return -(sum(gifts))


if __name__ == "__main__":
    sol = Solution()
    assert sol.pickGifts(gifts=[25, 64, 9, 4, 100], k=4) == 29
    assert sol.pickGifts(gifts=[1, 1, 1, 1], k=4) == 4
