from typing import List, Set, Tuple


class Solution:
    # Runtime: 8110 ms, faster than 41.10% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 50.74% of Python3 online submissions.
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        m, n = len(board), len(board[0])

        # So board[i][j] is already checked, it is infact equal to word[length]
        def search(i: int, j: int, length: int, visited: Set[Tuple[int, int]]):
            if self.found:
                return self.found
            if length == len(word) - 1:
                self.found = True
                return self.found
            for di, dj in neighbors:
                ii, jj = i + di, j + dj
                if (
                    0 <= ii < m
                    and 0 <= jj < n
                    and word[length + 1] == board[ii][jj]
                    and (ii, jj) not in visited
                ):
                    visited.add((ii, jj))
                    if self.found:
                        return self.found
                    search(ii, jj, length + 1, visited)
                    visited.remove((ii, jj))

            return self.found

        out = False
        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell == word[0]:
                    visited = set()
                    visited.add((row_idx, col_idx))
                    out = max(out, (search(row_idx, col_idx, 0, visited)))

        return out


sol = Solution()
assert sol.exist(
    board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"
)
assert sol.exist(
    board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"
)
assert not sol.exist(
    board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"
)
assert not sol.exist(board=[["A", "A"]], word="AAA")
assert sol.exist(
    [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS"
)
assert not sol.exist(
    board=[
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "B"],
        ["A", "A", "A", "A", "B", "A"],
    ],
    word="AAAAAAAAAAAAABB",
)
