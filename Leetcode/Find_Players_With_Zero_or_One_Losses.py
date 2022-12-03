from collections import defaultdict
from typing import List


class Solution:
    # Runtime: 1912 ms, faster than 93.63%.
    # Memory Usage: 68.7 MB, less than 77.41%.
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for win, loss in matches:
            if win not in d:
                d[win] = 0
            d[loss] += 1

        out = [sorted([i for i in d if d[i] == 0]), sorted(i for i in d if d[i] == 1)]
        return out
