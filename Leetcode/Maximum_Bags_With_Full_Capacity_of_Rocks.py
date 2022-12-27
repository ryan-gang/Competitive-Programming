from typing import List


class Solution:
    # Runtime: 950 ms, faster than 90.79%.
    # Memory Usage: 22 MB, less than 87.83%.
    # T : O(NLogN), S : O(N)
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        shortfalls = []
        for i, j in zip(capacity, rocks):
            shortfall = i - j
            shortfalls.append(shortfall)
        shortfalls.sort()
        idx = 0
        while additionalRocks > 0 and idx < len(shortfalls):
            additionalRocks -= shortfalls[idx]
            idx += 1
        return idx if additionalRocks >= 0 else idx - 1
