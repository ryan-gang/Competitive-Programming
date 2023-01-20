from typing import List, Set


class Solution:
    # Runtime: 103 ms, faster than 34.86% of Python3 online submissions for N-Queens II.
    # Memory Usage: 14 MB, less than 39.44% of Python3 online submissions for N-Queens II.
    def helper(self, boards: List[int], current_column: int, N: int):
        if current_column == N:
            self.allBoardsCount += 1
            return
        else:
            for j in range(N):
                # Try putting a Queen in every row and check if valid.
                boards[current_column] = j
                if self.checkValidity(boards, current_column):
                    self.helper(boards, current_column + 1, N)

    def checkValidity(self, boards: List[int], current_column: int):
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

    def totalNQueens(self, N: int) -> int:
        boards = [-1] * N
        self.allBoardsCount = 0
        (self.helper(boards, current_column=0, N=N))
        return self.allBoardsCount

    # Runtime: 53 ms, faster than 72.98%.
    # Memory Usage: 13.9 MB, less than 79.10%.
    # T : O(N), S : O(N)
    def totalNQueens2(self, n: int) -> int:
        """
        cols is a 1D array, representing each column, for each column in cols,
        we place a Queen in that column, represented by a int in cols[col].
        This should be unique in the cols array, and also there shouldn't be any
        2 queens on the same diagonal, for that we keep 2 sets, where we store the
        "formula" of the 2 diagonals passing through that row.
        As the 2 diagonals are +- 45 degrees from the X axis, the formulas are X + Y
        and X - Y. We make sure these sets don't have repeated values.
        And this is run for each column recursively.
        After every bad guess, we restore the value of the cols[col] to its inital value of -1.
        """
        self.out: int = 0
        self.n = n
        self.dfs(cols=[-1] * n, col=0, diag_positive=set(), diag_negative=set())
        return self.out

    def dfs(self, cols: List[int], col: int, diag_positive: Set[int], diag_negative: Set[int]):
        if col == self.n:
            self.out += 1
        for row in range(self.n):
            p, n = (row - col), (row + col)
            if row not in cols and p not in diag_positive and n not in diag_negative:
                cols[col] = row
                diag_negative.add(n)
                diag_positive.add(p)
                self.dfs(cols, col + 1, diag_positive, diag_negative)
                cols[col] = -1
                diag_positive.remove(p)
                diag_negative.remove(n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens2(15))
