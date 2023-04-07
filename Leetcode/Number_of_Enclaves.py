from collections import deque


class Solution:
    # Runtime: 657 ms, faster than 74.78%.
    # Memory Usage: 21.3 MB, less than 79.88%.
    # T : O(N), S : O(N) ; where N is the total cells in the grid.
    def numEnclaves(self, grid: list[list[int]]) -> int:
        """
        Just flash fill all islands connected to the edge. Convert them to 0.
        And then count the rest of the 'inner' islands.
        """
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        M, N = len(grid), len(grid[0])

        def flood_fill(r: int, c: int, val: int) -> int:
            count = 0
            seen: set[tuple[int, int]] = set()
            # We visit each island only once. The constraints are a bit too tight, so we need this.
            queue: deque[tuple[int, int]] = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                grid[r][c] = val
                count += 1
                for dr, dc in neighbors:
                    rr, cc = r + dr, c + dc
                    if (
                        rr >= 0
                        and rr < M
                        and cc >= 0
                        and cc < N
                        and grid[rr][cc] == 1
                        and (rr, cc) not in seen
                    ):
                        queue.append((rr, cc))
                        seen.add((rr, cc))
            return count

        # Flash fill all islands at the edges.
        for r in range(M):
            for c in range(N):
                if (r == 0 or r == M - 1 or c == 0 or c == N - 1) and (grid[r][c] == 1):
                    flood_fill(r, c, val=0)

        enclaves = 0
        # Just count the remaining islands.
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    enclaves += 1

        return enclaves


if __name__ == "__main__":
    sol = Solution()
    assert sol.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3
