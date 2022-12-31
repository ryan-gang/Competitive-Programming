from typing import List, Set, Tuple


class Solution:
    # Runtime: 89 ms, faster than 69.37%.
    # Memory Usage: 14 MB, less than 54.63%.
    # T : O(3^(MxN)), S : O(MxN)
    # Space for visited set only. Can hold max all elements in grid.
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.empty = 0
        self.m, self.n = len(grid), len(grid[0])
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    self.source = (r, c)
                elif cell == 2:
                    self.destination = (r, c)
                elif cell == 0:
                    self.empty += 1

        self.out = 0
        _ = set()
        _.add(self.source)
        self.dfs(self.source[0], self.source[1], _)
        return self.out

    def dfs(self, i, j, visited: Set[Tuple[int, int]]):
        if (i, j) == self.destination and len(visited) == self.empty + 2:
            self.out += 1
        for di, dj in self.directions:
            ii, jj = i + di, j + dj
            if (
                ii >= 0
                and ii < self.m
                and jj >= 0
                and jj < self.n
                and self.grid[ii][jj] != -1
                and (ii, jj) not in visited
            ):
                visited.add((ii, jj))
                self.dfs(ii, jj, visited)
                visited.remove((ii, jj))

    # Lee215.
    def uniquePathsIII_1(self, A):
        self.res = 0
        m, n, empty = len(A), len(A[0]), 1
        x = y = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0):
                return
            if A[x][y] == 2:
                self.res += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0

        dfs(x, y, empty)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    assert (sol.uniquePathsIII(grid=[[1, 2], [0, 0]])) == 1
    assert (sol.uniquePathsIII(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 2]])) == 2
    assert sol.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
    assert sol.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
