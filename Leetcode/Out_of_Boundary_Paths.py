from functools import lru_cache
import time


class Solution:
    # 73/94 passed. TLE. submissions/detail/748755614 (Just add the lru_cache)
    # Runtime: 174 ms, faster than 67.26%.
    # Memory Usage: 23.9 MB, less than 5.37%.
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m = m
        self.n = n
        self.max_val = pow(10, 9) + 7
        return int(self.paths(maxMove, startRow, startColumn)) % (self.max_val)

    @lru_cache(maxsize=None)
    def paths(self, maxMove: int, i: str, j: str):
        if maxMove == -1:
            return False
        elif i >= self.m or i < 0:
            return True
        elif j >= self.n or j < 0:
            return True
        else:
            return (
                self.paths(maxMove - 1, i - 1, j)
                + self.paths(maxMove - 1, i, j - 1)
                + self.paths(maxMove - 1, i + 1, j)
                + self.paths(maxMove - 1, i, j + 1)
            )


if __name__ == "__main__":
    sol = Solution()
    A = time.time()
    print(sol.findPaths(m=7, n=6, maxMove=13, startRow=0, startColumn=2))
    B = time.time()
    print("--- %s seconds ---" % round((B - A), 3))
