from collections import deque
from sys import maxsize


class Solution:
    # Runtime: 151 ms, faster than 6.26%.
    # Memory Usage: 20.4 MB, less than 8.47%.
    # T : O(N), S : O(N) ; where N is the total cells in the grid.
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        BFS + DP.
        We do a level wise traversal of the grid starting from the top left
        corner, and at every cell, we find the optimal cost to reach there. And
        repeat this until the final cell.
        """
        m, n = len(grid), len(grid[0])
        dp = [[maxsize for _ in range(n)] for __ in range(m)]
        dp[0][0] = grid[0][0]

        queue: deque[tuple[int, int]] = deque([(0, 0)])
        directions = [(0, 1), (1, 0)]  # right and down.
        seen: set[tuple[int, int]] = set()

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if rr >= 0 and rr < m and cc >= 0 and cc < n:
                    path_sum_upto_here: int = dp[r][c] + grid[rr][cc]
                    dp[rr][cc] = min(dp[rr][cc], path_sum_upto_here)
                    if (rr, cc) not in seen:
                        queue.append((rr, cc))
                        seen.add((rr, cc))

        return dp[-1][-1]

    # Runtime: 95 ms, faster than 84.59%.
    # Memory Usage: 15.7 MB, less than 46.72%.
    # T : O(N), S : O(1) ; where N is the total cells in the grid.
    # We update the original array, no extra space used.
    def minPathSum1(self, grid: list[list[int]]) -> int:
        """
        Traverse through the grid, updating the current cell, with the min cost
        of reaching to that cell. We only need to take into consideration the
        cell on the left and the one on the right.
        """
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[-1][-1]

    def minPathSum2(self, grid: list[list[int]]) -> int:
        """
        Same logic, cleaner code.
        """
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if r and c:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                elif r:
                    grid[r][c] += grid[r - 1][c]
                elif c:
                    grid[r][c] += grid[r][c - 1]

        return grid[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]) == 12
