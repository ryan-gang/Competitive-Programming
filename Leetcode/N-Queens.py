from StarterCode.decorators import timeit
from typing import List, Set, Tuple


# Runtime: 175 ms, faster than 20.74%.
# Memory Usage: 14.4 MB, less than 45.57%.
class Solution2:
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
        self.helper(boards, current_column=0, N=N)
        return [["." * i + "Q" + "." * (N - i - 1) for i in sol] for sol in self.allBoards]


class Solution:
    # Runtime: 3690 ms, faster than 5.01%.
    # Memory Usage: 14.6 MB, less than 5.94%.
    @timeit
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.out = []
        self.n = n
        self.place_queen(0, [], set(), set())
        out = self.parse_display(self.out)
        return out

    def parse_display(self, out):
        pretty_out = []
        for board in out:
            display = [["." for _ in range(self.n)] for __ in range(self.n)]
            for q in board:
                r, c = q
                display[r][c] = "Q"
            for i in range(self.n):
                display[i] = "".join(display[i])  # type: ignore
            pretty_out.append(display)

        return pretty_out

    def place_queen(self, row, queens: List[Tuple[int, int]], rows: Set[int], cols: Set[int]):
        if len(queens) == self.n:
            self.out.append(queens[:])
            return
        for r in range(row, self.n):
            if r in rows:
                continue
            for c in range(self.n):
                if c in cols:
                    continue
                flag = True
                for queen in queens:
                    rr, cc = queen
                    if Solution.check_validity(r, c, rr, cc):
                        flag = False
                        break
                if flag:
                    queens.append((r, c))
                    rows.add(r)
                    cols.add(c)
                    self.place_queen(r, queens, rows, cols)
                    queens.remove((r, c))
                    rows.remove(r)
                    cols.remove(c)

    @staticmethod
    def check_validity(r1: int, c1: int, r2: int, c2: int) -> bool:
        return (r1 - c1 == r2 - c2) or (r1 + c1 == r2 + c2)


# Is the best solution to this question ever ? Quite possibly.
# Ref : discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
class Solution3:
    """
    No need to store 2D array of queen placements. Just store a single 1D array, where index
    is the row number, and value of that index is the column number. Huge space saving.
    We can 1 have AT MOST 1 queen in each row, that is also easier to keep track here.
    To place a queen we need to check all the other placed queens, if they are in this
    diagonal or not, instead of O(N) computations, every try, just keep a track of all
    x - y and x + y, which is the thing checked for diagonal intersections.
    """

    @timeit
    def SolveNQueens(self, n):
        def DFS(queens, xy_diffs, xy_sums):
            r = len(queens)
            if r == n:
                out.append(queens[:])
                return None
            for c in range(n):
                if c not in queens and r - c not in xy_diffs and r + c not in xy_sums:
                    DFS(queens + [c], xy_diffs + [r - c], xy_sums + [r + c])

        out = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i + 1) for i in sol] for sol in out]


if __name__ == "__main__":
    sol = Solution()
    sol.solveNQueens(n=20)

    sol = Solution3()
    sol.SolveNQueens(n=20)
