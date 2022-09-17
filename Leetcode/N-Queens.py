from typing import List


# def helper(boards, current_column, N):
#     if current_column == N:
#         allBoards.append(boards[:])
#         return
#     else:
#         for j in range(N):
#             # Try putting a Queen in every row and check if valid.
#             boards[current_column] = j
#             if checkValidity(boards, current_column):
#                 helper(boards, current_column + 1, N)


# def checkValidity(boards, current_column):
#     # boards holds the row indices, so point co-ordinate is : (boards[i], i)
#     for col in range(current_column):
#         # Only required to check upto current column, later columns will be empty anyway.
#         x, y = col, boards[col]
#         p, q = current_column, boards[current_column]
#         if q == y:
#             return False
#         elif (x + y == p + q) or (x - y == p - q):
#             return False
#     return True


# Runtime: 175 ms, faster than 20.74% of Python3 online submissions for N-Queens.
# Memory Usage: 14.4 MB, less than 45.57% of Python3 online submissions for N-Queens.
class Solution:
    def helper(self, boards, current_column, N):
        if current_column == N:
            self.allBoards.append(boards[:])
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
        self.allBoards = []
        (self.helper(boards, current_column=0, N=N))
        return [["." * i + "Q" + "." * (N - i - 1) for i in sol] for sol in self.allBoards]


obj = Solution()
A = obj.solveNQueens(5)
print(A)
