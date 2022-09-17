from typing import List


class SolutionDFS:
    # Runtime: 478 ms, faster than 53.52% of Python3 online submissions.
    # Memory Usage: 16.6 MB, less than 50.32% of Python3 online submissions.
    def numIslandsdfs(self, grid: List[List[str]]) -> int:
        islands = 0
        self.m, self.n = len(grid), len(grid[0])
        if not grid:
            return 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    islands += 1

        return islands

    def dfs(self, grid, i, j):
        # Check for grid value, is there because dfs will call itself for all the neighbours.
        # In those cases need to weed out spurious calls.
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            self.dfs(grid, ii, jj)


class SolutionBFS:
    # Runtime: 678 ms, faster than 13.76% of Python3 online submissions.
    # Memory Usage: 16.2 MB, less than 91.69% of Python3 online submissions.
    def numIslandsbfs(self, grid: List[List[str]]) -> int:
        islands = 0
        self.m, self.n = len(grid), len(grid[0])
        if not grid:
            return 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.bfs(grid, [(i, j)])
                    islands += 1
        return islands

    def bfs(self, grid, coordinates):
        while coordinates:
            i, j = coordinates.pop()
            if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != "1":
                continue
            grid[i][j] = "#"
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii, jj = i + di, j + dj
                coordinates.append(grid, ii, jj)


# Ref : https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution

sol = SolutionDFS()
print(
    sol.numIslandsdfs(
        grid=[
            ["1", "1", "1", "0", "0"],
            ["1", "1", "0", "1", "0"],
            ["0", "1", "0", "0", "0"],
            ["1", "0", "0", "1", "1"],
        ]
    )
)
