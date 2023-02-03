from typing import List


class Solution:
    # Runtime: 58 ms, faster than 89.70%.
    # Memory Usage: 14.2 MB, less than 30.65%.
    # T : O(N), S : O(N)
    def convert1(self, s: str, numRows: int) -> str:
        """
        No need to keep track of cols, just append to the row.
        `move_row_wise` flips everytime we reach any of the rows at the ends. r = 0 or r = n-1.
        """
        idx, n, r = 0, len(s), 0

        grid = [[] for _ in range(numRows)]

        move_row_wise = 1
        if numRows == 1:
            return s
        while idx < n:
            grid[r].append(s[idx])
            idx += 1
            r += move_row_wise
            if r % (numRows - 1) == 0:
                move_row_wise *= -1

        out = ""
        for row in grid:
            out += "".join(row)

        return out

    def convert(self, s: str, numRows: int) -> str:
        """
        Keep a variable to denote the direction of travel, whenever we reach indices at the
        2 extremes, we reverse the direction.
        And keep moving in the direction.
        """
        dir, N = -1, len(s)
        n = idx = 0
        out: List[List[str]] = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        while n < N:
            out[idx].append(s[n])
            if idx == 0 or idx == numRows - 1:
                dir *= -1
            idx += dir
            n += 1

        return "".join(["".join(_) for _ in out])


if __name__ == "__main__":
    sol = Solution()
    assert (sol.convert(s="PAYPALISHIRING", numRows=1)) == "PAYPALISHIRING"
    assert (sol.convert(s="PAYPALISHIRING", numRows=2)) == "PYAIHRNAPLSIIG"
    assert (sol.convert(s="PAYPALISHIRING", numRows=3)) == "PAHNAPLSIIGYIR"
    assert (sol.convert(s="PAYPALISHIRING", numRows=4)) == "PINALSIGYAHRPI"
    assert (sol.convert(s="PAYPALISHIRING", numRows=5)) == "PHASIYIRPLIGAN"
