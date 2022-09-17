from typing import List


# Runtime: 103 ms, faster than 34.86% of Python3 online submissions for N-Queens II.
# Memory Usage: 14 MB, less than 39.44% of Python3 online submissions for N-Queens II.
class Solution:
    def helper(self, boards, current_column, N):
        if current_column == N:
            self.allBoardsCount += 1
            return
        else:
            for j in range(N):
                # Try putting a Queen in every row and check if valid.
                boards[current_column] = j
                if self.checkValidity(boards, current_column):
                    self.helper(boards, current_column + 1, N)

    def checkValidity(self, boards, current_column):
        # boards holds the row indices, so point co-ordinate is : (boards[i], i)
        for col in range(current_column):
            # Only required to check upto current column, later columns will be empty anyway.
            x, y = col, boards[col]
            p, q = current_column, boards[current_column]
            if q == y:
                return False
            elif (x + y == p + q) or (x - y == p - q):
                return False
        return True

    def solveNQueens(self, N: int) -> List[List[str]]:
        boards = [-1] * N
        self.allBoardsCount = 0
        (self.helper(boards, current_column=0, N=N))
        return self.allBoardsCount


obj = Solution()
A = obj.solveNQueens(1)
print(A)
