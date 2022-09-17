from typing import List, Set


class Solution:
    # 56 / 89 TC passed. TLE.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.start, self.end = (0, 0), (self.m - 1, self.n - 1)
        self.shortest_path_length = float("inf")
        v = set()
        if self.grid[0][0] == 0:
            v.add((0, 0))
            self.traverse(0, 0, 1, v)
        if self.shortest_path_length == float("inf"):
            return -1
        return self.shortest_path_length

    def traverse(self, i, j, path_length, visited_indices: Set):
        if path_length > self.shortest_path_length:
            return
        if (i, j) == self.end:
            self.shortest_path_length = min(self.shortest_path_length, path_length)
        for row in range(i - 1, i + 2):
            for col in range(j - 1, j + 2):
                if (
                    row >= 0
                    and row < self.m
                    and col >= 0
                    and col < self.n
                    and (row, col) != (i, j)
                    and (row, col) not in visited_indices
                    and self.grid[row][col] == 0
                ):
                    visited_indices.add((row, col))
                    self.traverse(row, col, path_length + 1, visited_indices)
                    visited_indices.remove((row, col))


class SolutionOnlyRightAndDownTraverse:
    # 62/89 TC passed. Wrong answer.
    # Because this code doesn't traverse left or upwards.
    # So TC like this : [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
    # Will break the code.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.start, self.end = (0, 0), (self.m - 1, self.n - 1)
        self.shortest_path_length = float("inf")
        if self.grid[0][0] == 0:
            self.traverse(0, 0, 1)
        if self.shortest_path_length == float("inf"):
            return -1
        return self.shortest_path_length

    def traverse(self, i, j, path_length):
        if path_length > self.shortest_path_length:
            return
        if (i, j) == self.end:
            self.shortest_path_length = min(self.shortest_path_length, path_length)
        for row in range(i, i + 2):
            for col in range(j, j + 2):
                if (
                    row >= 0
                    and row < self.m
                    and col >= 0
                    and col < self.n
                    and (row, col) != (i, j)
                    and self.grid[row][col] == 0
                ):
                    self.traverse(row, col, path_length + 1)


sol = Solution()
assert (sol.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]])) == 4
assert sol.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]])
assert sol.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]) == 2
print(
    sol.shortestPathBinaryMatrix(
        [
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
        ]
    )
)
