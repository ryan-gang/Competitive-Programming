from typing import List


class Solution:
    """All cells that satisfy the equation r - c = N, fall on the same diagonal.
    So we keep a track of the value of any one cell in that diagonal,
    and then match with all the other values in the diagonal."""

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if (r - c) in d:
                    if d[r - c] != cell:
                        return False
                else:
                    d[r - c] = cell
        return True

    """Make sure all the cells, have the same value as their upper left neighbour."""

    def isToeplitzMatrix1(self, matrix: List[List[int]]) -> bool:
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False

        return True

    def isToeplitzMatrixAlternateTo1(self, matrix):
        return all(
            r == 0 or c == 0 or matrix[r - 1][c - 1] == val
            for r, row in enumerate(matrix)
            for c, val in enumerate(row)
        )
