class Solution:
    def set_col_to_zero(self, col: int):
        for row in self.matrix:
            row[col] = 0

    def set_row_to_zero(self, row: int):
        self.matrix[row] = [0 for _ in range(self.c)]

    # Runtime: 332 ms, faster than 21.84% of Python3 online submissions.
    # Memory Usage: 14.9 MB, less than 16.32% of Python3 online submissions.
    # T : O(N^2), S : O(1)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self.r, self.c = len(matrix), len(matrix[0])
        # Bool to indicate if row 0 contains 0, and if we need to convert entire row to 0's.
        transform_row0 = False
        transform_col0 = False  # Same for col 0.

        for row_idx, row in enumerate(matrix):
            for col_idx, cell in enumerate(row):
                if cell == 0:
                    matrix[0][col_idx] = 0
                    matrix[row_idx][0] = 0
                    if row_idx == 0:
                        transform_row0 = True
                    if col_idx == 0:
                        transform_col0 = True

        for col_idx, col in enumerate(matrix[0]):
            if col_idx > 0 and col == 0:
                self.set_col_to_zero(col_idx)

        col0 = [matrix[row][0] for row in range(self.r)]
        for row_idx, row in enumerate(col0):
            if row_idx > 0 and row == 0:
                self.set_row_to_zero(row_idx)

        if transform_row0:
            self.set_row_to_zero(0)

        if transform_col0:
            self.set_col_to_zero(0)

    # Runtime: 126 ms, faster than 90.45%.
    # Memory Usage: 14.9 MB, less than 25.71%.
    # T : O(N^2), S : O(1)
    def setZeroes1(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self.r, self.c = len(matrix), len(matrix[0])
        rows: set[int] = set()  # Add row indices to rows, will set these rows to 0.
        cols: set[int] = set()  # Add col indices to cols, will set these cols to 0.
        for row_idx, row in enumerate(matrix):
            for col_idx, cell in enumerate(row):
                if cell == 0:
                    rows.add(row_idx)
                    cols.add(col_idx)

        for col_idx in cols:
            self.set_col_to_zero(col_idx)
        for row_idx in rows:
            self.set_row_to_zero(row_idx)


# LeetCode editorial.
class Solution2(object):
    def setZeroes(self, matrix: list[list[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column
            # is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the
                # corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using
        # the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0


if __name__ == "__main__":
    sol = Solution()

    sol.setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert sol.matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    sol.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    assert sol.matrix == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ]
