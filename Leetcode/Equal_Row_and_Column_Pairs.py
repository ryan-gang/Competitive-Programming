from collections import defaultdict
from typing import Sequence, Mapping


class Solution:
    # T : O(N^2), S : O(N^2)
    # Same time complexity as the Trie solution.
    def equalPairs(self, grid: list[list[int]]) -> int:
        self.col_set: Mapping[Sequence[int], int] = defaultdict(int)
        self.count = 0
        for r, row in enumerate(grid):
            col: list[int] = []
            for c, _ in enumerate(row):
                col.append(grid[c][r])
            self.col_set[tuple(col)] += 1
        for r, row in enumerate(grid):
            if (R := tuple(row)) in self.col_set:
                self.count += self.col_set[R]

        print(self.col_set, self.count)
        return self.count


if __name__ == "__main__":
    sol = Solution()
    assert sol.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1
    assert sol.equalPairs(grid=[[13, 13], [13, 13]]) == 4
