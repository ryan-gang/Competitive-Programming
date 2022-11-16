from typing import List
from StarterCode.Union_Find import Union


# Ref : discuss/56340/Python-Simple-DFS-Solution
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
        # Check for grid value, because dfs will call itself for all the neighbours.
        # In those cases need to weed out spurious calls.
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            self.dfs(grid, ii, jj)


class SolutionDFS2:
    """
    To keep track of the visited islands, and not recount them,
    we rewrite them from "1" to "#".
    If we encounter a "1", we dfs over all of its neighbours, and change them to "#",
    it is one island only. And repeat this for all the "1"s.
    We iterate over self.grid, and also change self.grid itself.
    """

    # Runtime: 750 ms, faster than 21.00% of Python3 online submissions.
    # Memory Usage: 16.4 MB, less than 81.29% of Python3 online submissions.
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        islands = 0

        for i_idx, row in enumerate(self.grid):
            for j_idx, cell in enumerate(row):
                if cell == "1":
                    self.dfs(i_idx, j_idx)
                    islands += 1

        return islands

    def dfs(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.grid[i][j] != "1":
            return
        self.grid[i][j] = "#"
        if i > 0:
            self.dfs(i - 1, j)
        if i < self.m - 1:
            self.dfs(i + 1, j)
        if j > 0:
            self.dfs(i, j - 1)
        if j < self.n - 1:
            self.dfs(i, j + 1)


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


# Runtime: 1325 ms, faster than 5.03% of Python3 online submissions.
# Memory Usage: 18.4 MB, less than 39.00% of Python3 online submissions.
class Solution:
    """
    Initially take a pass over the grid, add all islands as their own "sets"
    in the Union Find data structure. In the second pass over grid, all nodes
    and their neighbouring nodes will be "union"-ed, everytime we union we
    reduce the count of islands by 1.
    Finally we can return count of islands.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        L = ((m * n) + 1)
        uf = Union(L)
        islands = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "1":
                    node = r * n + c
                    uf.new(node)
                    islands += 1

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "1":
                    node1 = r * n + c
                    """
                    Instead of searching through all the 4 directional neighbours, we can just
                    look at 2 directions, bottom and right. All left and up have already been
                    seen, DSU is also undirected.
                    """
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        rr, cc = r + dr, c + dc
                        if rr >= 0 and rr < m and cc >= 0 and cc < n and grid[rr][cc] == "1":
                            node2 = rr * n + cc
                            res = uf.union(node1, node2)
                            if res:
                                islands -= 1

        return islands


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.numIslands(
            grid=[
                ["1", "1", "1", "0", "0"],
                ["1", "1", "0", "1", "0"],
                ["0", "1", "0", "0", "0"],
                ["1", "0", "0", "1", "1"],
            ]
        )
    )
