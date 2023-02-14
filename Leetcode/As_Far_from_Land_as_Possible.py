from collections import deque


class Solution:
    # Runtime: 496 ms, faster than 95.80%.
    # Memory Usage: 14.5 MB, less than 73.6%.
    # T : O(N * N), S : O(N * N)
    def maxDistance(self, grid: list[list[int]]) -> int:
        """
        We use a multi source BFS, where we start the BFS from multiple starting points.
        At each cell it checks if the current value is = 0, ie not visited.
        And adds that index to the queue, and changes the value to 1.
        Because we don't want to visit this cell again.
        Same thing can also be implemented using a set, keep track of visited indices.
        """
        queue: deque[tuple[int, int]] = deque()

        dist = -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(grid)

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    queue.append((r, c))

        if not queue or len(queue) == n * n:  # No land, or no water.
            return -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if rr >= 0 and cc >= 0 and rr < n and cc < n and grid[rr][cc] == 0:
                        # Traverse to neighbor only if it hasn't been visited.
                        # And mark this visit, by changing its value to 1.
                        queue.append((rr, cc))
                        grid[rr][cc] = 1
            dist += 1
        return dist

    # Runtime: 620 ms, faster than 65.11%.
    # Memory Usage: 15.8 MB, less than 18.23%.
    # T : O(N * N), S : O(N * N)
    def maxDistance1(self, grid: list[list[int]]) -> int:
        queue: deque[tuple[int, int]] = deque()
        visited: set[tuple[int, int]] = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(grid)
        dist = -1

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    queue.append((r, c))
                    visited.add((r, c))

        if not queue or len(queue) == n * n:
            return -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if rr >= 0 and cc >= 0 and rr < n and cc < n and (rr, cc) not in visited:
                        queue.append((rr, cc))
                        visited.add((rr, cc))
            dist += 1
        return dist


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxDistance(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
    assert sol.maxDistance(grid=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert (
        sol.maxDistance(
            grid=[
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
            ]
        )
        == 2
    )
