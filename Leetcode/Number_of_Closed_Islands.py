from collections import deque


class Solution:
    # Runtime: 198 ms, faster than 5.12%.
    # Memory Usage: 14.4 MB, less than 61.65%.
    # T : O(N), S : O(N) ; where N is the total number of cells.
    # We visit each 0 cell once. But visit 1's at most thrice.
    def closedIsland(self, grid: list[list[int]]) -> int:
        """
        All the cells with 0 that are directly/indirectly connected to any of
        the edges, cannot be surrounded by water on all sides, so we replace all
        such 0's with 1's. Then we just find the number of connected components
        in the grid, because if any of the component is not connected to the
        edge, it HAS to be CLOSED by water on all sides. At which point, that we
        need not worry about. So we can just count all components, and keep on
        converting them to 1's.
        """

        def flood_fill_neighbors(r: int, c: int, val: int):
            queue: deque[tuple[int, int]] = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                grid[r][c] = val
                for dr, dc in neighbors:
                    rr, cc = r + dr, c + dc
                    if rr >= 0 and rr < M and cc >= 0 and cc < N and grid[rr][cc] == 0:
                        queue.append((rr, cc))

        M, N = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in [0, len(grid) - 1]:
            for col in range(N):
                if grid[row][col] == 0:
                    flood_fill_neighbors(row, col, val=1)

        for col in [0, len(grid[0]) - 1]:
            for row in range(M):
                if grid[row][col] == 0:
                    flood_fill_neighbors(row, col, val=1)

        islands = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 0:
                    islands += 1
                    flood_fill_neighbors(r, c, val=1)
        return islands


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.closedIsland(
            grid=[
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ]
        )
        == 2
    )
