from collections import deque
from typing import Deque


class Solution:
    """
    Both solutions utilise BFS to find the shortest distance, in the first one
    we do level wise traversal of the queue, and keep track of levels. In the
    second one we store the level, inside the queue with every element.
    """
    # T : O(N ^ 2), S : O(N)
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n, length = len(grid), 1
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        queue: Deque[tuple[int, int]] = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        diff = [-1, 0, 1]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return length
                for dr in diff:
                    for dc in diff:
                        rr, cc = r + dr, c + dc
                        if (
                            0 <= rr < n
                            and 0 <= cc < n
                            and grid[rr][cc] == 0
                            and (not (dr == dc == 0))
                        ):
                            queue.append((rr, cc))
                            grid[rr][cc] = 1

            length += 1

        return -1

    def shortestPathBinaryMatrix1(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            # If start or end cells are already 1 we can't step on them.
            return -1
        q: list[tuple[int, int, int]] = [(0, 0, 1)]  # row, col, distance
        grid[0][0] = 1
        diff = [-1, 0, 1]
        for i, j, d in q:
            if i == n - 1 and j == n - 1:
                return d
            for xx in diff:
                for yy in diff:
                    x, y = i + xx, j + yy
                    if (
                        (xx != 0 or yy != 0)
                        and 0 <= x < n
                        and 0 <= y < n
                        and grid[i + xx][j + yy] == 0
                    ):
                        grid[x][y] = 1
                        q.append((x, y, d + 1))
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert (sol.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]])) == 4
    assert sol.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert sol.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]) == 2
    assert (
        sol.shortestPathBinaryMatrix(
            [[0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]]
        )
        == -1
    )
