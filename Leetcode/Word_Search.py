from typing import List, Set, Tuple
from StarterCode.decorators import timeit


class Solution:
    # Runtime: 8110 ms, faster than 41.10% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 50.74% of Python3 online submissions.
    @timeit
    def exist2(self, board: List[List[str]], word: str) -> bool:
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

    @timeit
    # Runtime: 5543 ms, faster than 52.66%.
    # Memory Usage: 14 MB, less than 13.61%.
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        search() takes the current string, its indices and checks the neighbouring
        letters around it to find the next letter. Checks if we can create our required
        string from this current one, and then recurses.
        """
        self.found = False
        neighbors = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        m, n = len(board), len(board[0])
        words = set([word[:i] for i in range(1, len(word) + 1)])

        def search(r, c, string, visited):
            if string == word:
                self.found = True
                return self.found
            for dr, dc in neighbors:
                rr, cc = r + dr, c + dc
                if rr >= 0 and cc >= 0 and rr < m and cc < n and (rr, cc) not in visited:
                    string += board[rr][cc]
                    if string in words:
                        visited.add((rr, cc))
                        search(rr, cc, string, visited)
                        visited.remove((rr, cc))
                    string = string[:-1]

        visited = set()
        for r in range(m):
            for c in range(n):
                if board[r][c] in words:
                    visited.add((r, c))
                    search(r, c, board[r][c], visited)
                    visited.remove((r, c))
        return self.found


if __name__ == "__main__":
    sol = Solution()
    assert sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    assert sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    assert not sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
    assert not sol.exist([["A", "A"]], "AAA")
    assert sol.exist(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"
    )
    assert not sol.exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "B"],
            ["A", "A", "A", "A", "B", "A"],
        ],
        "AAAAAAAAAAAAABB",
    )
