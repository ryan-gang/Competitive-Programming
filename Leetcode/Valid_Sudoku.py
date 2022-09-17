from collections import defaultdict
from typing import List


# Runtime: 213 ms, faster than 6.54% of Python3 online submissions...
# Memory Usage: 13.8 MB, less than 81.20% of Python3 online submissions...
class Solution:
    def parseCell(self, dictionary: dict[str, int], key: str, val: int) -> bool:
        temp: int = dictionary.get(key, 0)
        temp = temp | (1 << val)
        if temp == dictionary.get(key):
            return False
        else:
            dictionary[key] = temp
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols: dict = defaultdict(int)
        rows: dict = defaultdict(int)
        subs: dict = defaultdict(int)

        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                row_index, col_index, sub_index = i, j, f"{i // 3}{j // 3}"
                if cell != ".":
                    r = self.parseCell(dictionary=rows, key=str(row_index), val=int(cell))
                    c = self.parseCell(dictionary=cols, key=str(col_index), val=int(cell))
                    s = self.parseCell(dictionary=subs, key=sub_index, val=int(cell))
                    if not (r and c and s):
                        return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
sol = Solution()
print(sol.isValidSudoku(board))


# Runtime: 122 ms, faster than 58.52% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.9 MB, less than 81.20% of Python3 online submissions for Valid Sudoku.
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen: set = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                row_index, col_index, sub_index = i, j, f"{i // 3}{j // 3}"
                if cell != ".":
                    row_string = f"{cell} in row {row_index}"
                    col_string = f"{cell} in col {col_index}"
                    sub_string = f"{cell} in sub {sub_index}"
                    if row_string in seen or col_string in seen or sub_string in seen:
                        return False
                    else:
                        seen.update({row_string, col_string, sub_string})
        return True
