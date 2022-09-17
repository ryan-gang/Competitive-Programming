from typing import List


class Solution:
    # Runtime: 183 ms, faster than 70.48% of Python3 online submissions.
    # Memory Usage: 16.6 MB, less than 48.04% of Python3 online submissions.
    # T : O(m*n), S : O(1)
    # Auxiliary space : O(m*n) -> recursion stack size.
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        VISITED = -1
        max_size = 0

        def dfs(i: int, j: int, size: int) -> int:
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                size += 1
                grid[i][j] = VISITED
                size = dfs(i - 1, j, size)
                size = dfs(i + 1, j, size)
                size = dfs(i, j - 1, size)
                size = dfs(i, j + 1, size)
            return size

        for r in range(m):
            for c in range(n):
                size = dfs(r, c, 0)
                max_size = max(size, max_size)
        return max_size


sol = Solution()
print(
    sol.maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)
