from typing import List


# Runtime: 5613 ms, faster than 6.62% of Python3 online submissions...
# Memory Usage: 26.3 MB, less than 10.49% of Python3 online submissions...
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cols = len(self.matrix[0])
        self.rows = len(self.matrix)
        # self.rowSums = []
        # for row in self.matrix:
        #     self.rowSums.append(sum(row))
        self.dp = [[0 for i in range(self.cols + 1)] for j in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.dp[i][j + 1] = self.dp[i][j] + self.matrix[i][j]
        print(self.dp)

    # 12/24 TC, TLE.
    def sumRegionUnoptimised(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.sum += self.matrix[i][j]

        return self.sum

    # 13/24 TC, TLE.
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.sum = 0
        if (col2 - col1 + 1) > self.cols // 2:
            remainingCols = set(range(self.cols)) - set(range(col1, col2 + 1))
            for i in range(row1, row2 + 1):
                self.sum += self.rowSums[i]
                for j in remainingCols:
                    self.sum -= self.matrix[i][j]
        else:
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    self.sum += self.matrix[i][j]

        return self.sum

    def sumRegionOptimised(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.sum = 0
        for row in range(row1, row2 + 1):
            self.sum += self.dp[row][col2 + 1] - self.dp[row][col1]
        return self.sum


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegionOptimised(row1=2, col1=1, row2=4, col2=3))
print(obj.sumRegionOptimised(1, 1, 2, 2))
print(obj.sumRegionOptimised(1, 2, 2, 4))
