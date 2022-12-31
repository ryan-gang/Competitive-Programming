class Solution:
    # Runtime: 58 ms, faster than 89.70%.
    # Memory Usage: 14.2 MB, less than 30.65%.
    # T : O(N), S : O(N)
    def convert(self, s: str, numRows: int) -> str:
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


if __name__ == "__main__":
    sol = Solution()
    assert (sol.convert(s="PAYPALISHIRING", numRows=1)) == "PAYPALISHIRING"
    assert (sol.convert(s="PAYPALISHIRING", numRows=2)) == "PYAIHRNAPLSIIG"
    assert (sol.convert(s="PAYPALISHIRING", numRows=3)) == "PAHNAPLSIIGYIR"
    assert (sol.convert(s="PAYPALISHIRING", numRows=4)) == "PINALSIGYAHRPI"
    assert (sol.convert(s="PAYPALISHIRING", numRows=5)) == "PHASIYIRPLIGAN"
