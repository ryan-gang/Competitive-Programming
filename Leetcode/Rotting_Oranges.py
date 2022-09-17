from collections import deque
from typing import List


class Solution:
    # Runtime: 99 ms, faster than 25.28% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 47.41% of Python3 online submissions.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = deque()
        minutes_passed = fresh = 0
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 2:
                    rotten.append((i, j))
                elif cell == 1:
                    fresh += 1

        while rotten and fresh > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx >= 0 and xx < m and yy >= 0 and yy < n:
                        if grid[xx][yy] == 1:
                            fresh -= 1
                            grid[xx][yy] = 2
                            rotten.append((xx, yy))

        return minutes_passed if fresh == 0 else -1


sol = Solution()
print(sol.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
