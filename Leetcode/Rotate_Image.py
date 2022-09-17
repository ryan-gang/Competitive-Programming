from typing import List

# Rotate groups of 4 cells at a time.
# This way no extra space is required, we swap one by one.
# T : O(N*N), S : O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


# Reverse on diagonal, and then reverse left to right.
# Transpose and Reflect.
# T : O(N*N), S : O(1)
class Solution2:
    # Runtime: 75 ms, faster than 9.93% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 74.32% of Python3 online submissions.
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
